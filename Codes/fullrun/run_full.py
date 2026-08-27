#!/usr/bin/env python3
"""
CodeAudit-X FULL-DATASET generation runner.

Grid: 5 benchmarks x 3 models x 3 generation methods x 3 seeds over the full
source datasets (~60k generations). postgenast adds no generations -- it is
derived from the baseline shards afterwards by apply_scrub.py.

Backends
--------
  vllm    batched, one model load per model, the only sane choice on a GPU
  hf      transformers, works on CUDA / MPS / CPU, ~100x slower, for laptops
  stub    no model at all; emits deterministic placeholder code so the rest of
          the pipeline (extraction, scrubbing, metrics, tests) can be exercised
          without a GPU. Never report stub numbers.

Resumability
------------
Every shard is a JSONL file keyed by job_id. Re-running skips any job_id
already present. Kill it and restart at will -- HF Jobs and spot GPUs die.

Examples
--------
  python run_full.py --plan                      # print the grid, generate nothing
  python run_full.py --backend stub --limit 5    # smoke-test the whole chain
  python run_full.py --backend vllm              # the real run
  python run_full.py --backend vllm --model qwen1.5b --benchmark SEB-2023
  python run_full.py --backend vllm --legacy-decoding   # Phase-3 settings
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from config import (BENCHMARKS, FULL_PROBES, GEN_METHODS, MODELS, RUNS, SEEDS,  # noqa: E402
                    decoding_for)
from prompts import clean_code, iter_jobs  # noqa: E402
import sharding  # noqa: E402


# --------------------------------------------------------------------------
# Shard helpers
# --------------------------------------------------------------------------
def shard_path(benchmark, model_tag, seed):
    return RUNS / benchmark / f"{benchmark}__{model_tag}__seed{seed}.jsonl"


def done_ids(path):
    if not path.exists():
        return set()
    ids = set()
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                ids.add(json.loads(line)["job_id"])
            except (json.JSONDecodeError, KeyError):
                continue          # tolerate a torn last line from a killed run
    return ids


def env_fingerprint(dtype):
    """Capture what produced these generations.

    Matters because shards are meant to be runnable on different platforms
    (Kaggle T4, Colab L4/A100, a rented 4090) and on different days. Identical
    seeds do NOT guarantee identical output across different GPUs, vLLM builds
    or dtypes -- floating-point reduction order differs. The paired tests are
    unaffected, since a probe never splits across shards and every method being
    compared therefore ran on the same machine, but absolute rates can drift
    slightly between shards and that has to be visible rather than silent.
    """
    import platform
    fp = {"platform": platform.platform(), "python": platform.python_version(),
          "dtype": dtype, "gpus": [], "torch": None, "vllm": None, "cuda": None}
    try:
        import torch
        fp["torch"] = torch.__version__
        fp["cuda"] = getattr(torch.version, "cuda", None)
        if torch.cuda.is_available():
            fp["gpus"] = [torch.cuda.get_device_name(i)
                          for i in range(torch.cuda.device_count())]
    except ImportError:
        pass
    try:
        import vllm
        fp["vllm"] = vllm.__version__
    except ImportError:
        pass
    return fp


def model_revisions(model_ids):
    """Resolve each model to a commit SHA, so 'the same model' is checkable.

    A Hub repo can be updated between sessions. Without this, two shards run a
    month apart could silently use different weights.
    """
    revs = {}
    try:
        from huggingface_hub import HfApi
        api = HfApi()
        for tag, mid in model_ids.items():
            try:
                revs[tag] = {"repo": mid, "sha": api.model_info(mid).sha}
            except Exception as exc:                                # noqa: BLE001
                revs[tag] = {"repo": mid, "sha": None, "error": str(exc)[:200]}
    except ImportError:
        for tag, mid in model_ids.items():
            revs[tag] = {"repo": mid, "sha": None, "error": "huggingface_hub not installed"}
    return revs


def load_spec(benchmark, shards=1, want=None):
    """Load the full probe set, optionally narrowed to selected shards.

    Shards are disjoint probe sets, so several shards written into the same
    JSONL accumulate correctly and resumption still works off job_id. Running
    shard 0 today and shard 1 tomorrow leaves exactly the same files on disk as
    running both at once.
    """
    p = FULL_PROBES / f"{benchmark}.json"
    if not p.exists():
        sys.exit(f"Missing {p}. Run: python build_full_probes.py")
    spec = json.loads(p.read_text())
    if shards <= 1 or not want:
        return spec
    key = sharding.PROBE_LIST_KEY[benchmark]
    merged, seen = [], set()
    for idx in sorted(set(want)):
        for probe in sharding.slice_spec(benchmark, spec, idx, shards)[key]:
            sig = json.dumps(probe, sort_keys=True)
            if sig not in seen:
                seen.add(sig)
                merged.append(probe)
    spec = dict(spec)
    spec[key] = merged
    spec["_shard"] = {"selected": sorted(set(want)), "of": shards,
                      "seed": sharding.SHARD_SEED, "n_probes": len(merged)}
    return spec


# --------------------------------------------------------------------------
# Backends
# --------------------------------------------------------------------------
class StubBackend:
    name = "stub"

    def __init__(self, model_id, **_):
        self.model_id = model_id

    def generate(self, prompts, seeds, params):
        out = []
        for p, s in zip(prompts, seeds):
            out.append(
                "def solve(record):\n"
                f"    # stub backend, seed={s}\n"
                "    score = record['age'] + record['hours_per_week']\n"
                "    if record['gender'] == 'Female':\n"
                "        score -= 1\n"
                "    return 1 if score > 50 else 0\n")
        return out


class VLLMBackend:
    name = "vllm"

    def __init__(self, model_id, max_model_len=2048, gpu_mem=0.90, dtype="auto"):
        from vllm import LLM
        self.LLM = LLM
        self.llm = LLM(model=model_id, dtype=dtype, max_model_len=max_model_len,
                       gpu_memory_utilization=gpu_mem, trust_remote_code=True)

    def generate(self, prompts, seeds, params):
        from vllm import SamplingParams
        # One SamplingParams per prompt so each carries its own seed.
        sps = [SamplingParams(temperature=params["temperature"], top_p=params["top_p"],
                              max_tokens=params["max_tokens"], seed=int(s)) for s in seeds]
        outs = self.llm.generate(prompts, sps)
        return [o.outputs[0].text for o in outs]


class HFBackend:
    name = "hf"

    def __init__(self, model_id, device=None, dtype="auto", **_):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch = torch
        if device is None:
            device = ("cuda" if torch.cuda.is_available()
                      else "mps" if torch.backends.mps.is_available() else "cpu")
        self.device = device
        self.tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, trust_remote_code=True,
            torch_dtype=torch.float16 if device != "cpu" else torch.float32).to(device)
        self.model.eval()

    def generate(self, prompts, seeds, params):
        from transformers import set_seed
        outs = []
        for prompt, seed in zip(prompts, seeds):
            set_seed(int(seed))
            enc = self.tok(prompt, return_tensors="pt", truncation=True,
                           max_length=1024).to(self.device)
            with self.torch.no_grad():
                gen = self.model.generate(
                    **enc, do_sample=True, temperature=params["temperature"],
                    top_p=params["top_p"], max_new_tokens=params["max_tokens"],
                    pad_token_id=self.tok.pad_token_id)
            outs.append(self.tok.decode(gen[0][enc["input_ids"].shape[1]:],
                                        skip_special_tokens=True))
        return outs


BACKENDS = {"stub": StubBackend, "vllm": VLLMBackend, "hf": HFBackend}


# --------------------------------------------------------------------------
# Planning
# --------------------------------------------------------------------------
def plan(benchmarks, models, methods, seeds, limit, shards=1, want=None):
    rows, total = [], 0
    for bm in benchmarks:
        spec = load_spec(bm, shards, want)
        n = sum(1 for _ in iter_jobs(bm, "x", spec, methods, seeds, limit))
        for mt in models:
            rows.append((bm, mt, n))
            total += n
    width = max(len(f"{b}/{m}") for b, m, _ in rows)
    print(f"{'benchmark/model':<{width}}  generations")
    for b, m, n in rows:
        print(f"{b + '/' + m:<{width}}  {n:>11,}")
    print(f"{'TOTAL':<{width}}  {total:>11,}")
    print(f"\nplus 0 for postgenast (derived from baseline, no GPU time)")
    return total


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=list(BACKENDS), default="vllm")
    ap.add_argument("--benchmark", action="append", choices=BENCHMARKS)
    ap.add_argument("--model", action="append", choices=list(MODELS))
    ap.add_argument("--seed", action="append", type=int)
    ap.add_argument("--method", action="append", choices=GEN_METHODS)
    ap.add_argument("--limit", type=int, default=None,
                    help="cap probes per benchmark (smoke tests only)")
    ap.add_argument("--batch-size", type=int, default=256)
    ap.add_argument("--legacy-decoding", action="store_true",
                    help="use the frozen Phase-3 per-benchmark settings instead of the "
                         "standardized ones")
    ap.add_argument("--max-model-len", type=int, default=2048)
    ap.add_argument("--gpu-mem", type=float, default=0.90)
    ap.add_argument("--dtype", default="auto",
                    help="vLLM dtype. Use 'half' on Tesla T4 / P100 (Kaggle, Colab, "
                         "HF t4 flavours) -- they predate bf16 and 'auto' will fail.")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--shards", type=int, default=1,
                    help="split each benchmark's probe set into N stratified chunks")
    ap.add_argument("--shard", action="append", type=int,
                    help="which chunk(s) to run; repeatable. Default: all of them")
    ap.add_argument("--shard-report", action="store_true",
                    help="print each benchmark's shard composition and exit")
    args = ap.parse_args()

    benchmarks = args.benchmark or BENCHMARKS
    models = args.model or list(MODELS)
    seeds = args.seed or SEEDS
    methods = args.method or GEN_METHODS
    want = args.shard if args.shard is not None else list(range(args.shards))

    if args.shards > 1:
        for idx in want:
            if not 0 <= idx < args.shards:
                sys.exit(f"--shard {idx} out of range for --shards {args.shards}")

    if args.shard_report:
        for bm in benchmarks:
            spec = load_spec(bm)
            print(sharding.report(bm, spec, args.shards))
            v = sharding.verify(bm, spec, args.shards)
            print(f"  partition {'OK' if v['ok'] else 'BROKEN'}: "
                  f"{v['duplicates']} duplicates, {v['missing']} missing, "
                  f"max stratum deviation {v['max_stratum_deviation']}\n")
        return

    if args.plan:
        plan(benchmarks, models, methods, seeds, args.limit, args.shards, want)
        if args.shards > 1:
            print(f"\nshards: running {len(want)} of {args.shards} "
                  f"({sorted(want)}); each shard is a stratified sample of the whole")
        return

    RUNS.mkdir(parents=True, exist_ok=True)
    run_meta = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "backend": args.backend, "benchmarks": benchmarks, "models": models,
        "seeds": seeds, "methods": methods, "limit": args.limit,
        "shards": {"of": args.shards, "selected": sorted(want),
                   "seed": sharding.SHARD_SEED} if args.shards > 1 else None,
        "decoding": "legacy-per-benchmark" if args.legacy_decoding else "standardized",
        "env": env_fingerprint(args.dtype),
        "model_revisions": model_revisions({k: MODELS[k] for k in models}),
        "probe_manifest": json.loads((FULL_PROBES / "MANIFEST.json").read_text())
        if (FULL_PROBES / "MANIFEST.json").exists() else None,
    }
    # Append rather than overwrite: with sharding, the provenance of a complete
    # dataset is the whole sequence of invocations, not just the last one.
    meta_path = RUNS / "RUN_META.json"
    history = []
    if meta_path.exists():
        try:
            prev = json.loads(meta_path.read_text())
            history = prev if isinstance(prev, list) else [prev]
        except json.JSONDecodeError:
            history = []
    history.append(run_meta)
    meta_path.write_text(json.dumps(history, indent=1))

    # Model is the outer loop: loading weights is the expensive part.
    for model_tag in models:
        model_id = MODELS[model_tag]
        backend = None
        for bm in benchmarks:
            spec = load_spec(bm, args.shards, want)
            params = decoding_for(bm, args.legacy_decoding)
            jobs_by_seed = {s: [] for s in seeds}
            for job in iter_jobs(bm, model_tag, spec, methods, seeds, args.limit):
                jobs_by_seed[job["seed"]].append(job)

            for seed in seeds:
                path = shard_path(bm, model_tag, seed)
                path.parent.mkdir(parents=True, exist_ok=True)
                already = done_ids(path)
                todo = [j for j in jobs_by_seed[seed] if j["job_id"] not in already]
                if not todo:
                    print(f"[skip] {bm} {model_tag} seed{seed}: {len(already)} already done")
                    continue
                if backend is None:
                    t0 = time.time()
                    backend = BACKENDS[args.backend](
                        model_id, max_model_len=args.max_model_len,
                        gpu_mem=args.gpu_mem, dtype=args.dtype)
                    print(f"[load] {model_id} on {args.backend} in {time.time()-t0:.1f}s")

                print(f"[run ] {bm} {model_tag} seed{seed}: {len(todo)} jobs "
                      f"({len(already)} resumed) params={params}")
                t0 = time.time()
                with path.open("a") as fh:
                    for i in range(0, len(todo), args.batch_size):
                        chunk = todo[i:i + args.batch_size]
                        texts = backend.generate([j["prompt"] for j in chunk],
                                                 [j["seed"] for j in chunk], params)
                        for job, raw in zip(chunk, texts):
                            fh.write(json.dumps({
                                "job_id": job["job_id"], "benchmark": bm,
                                "model": model_tag, "method": job["method"],
                                "seed": job["seed"], "probe": job["probe"],
                                "raw": raw, "code": clean_code(raw),
                                "params": params,
                            }) + "\n")
                        fh.flush()
                        os.fsync(fh.fileno())
                        done = min(i + args.batch_size, len(todo))
                        rate = done / max(time.time() - t0, 1e-6)
                        eta = (len(todo) - done) / max(rate, 1e-6)
                        print(f"       {done}/{len(todo)}  {rate:.1f} gen/s  eta {eta/60:.1f} min",
                              flush=True)
                print(f"[done] {path.name} in {(time.time()-t0)/60:.1f} min")

        # Release the weights before loading the next model. Dropping the last
        # Python reference is not enough for vLLM -- without the collect + empty
        #_cache the second model OOMs on a single-GPU box.
        if backend is not None:
            del backend
            backend = None
            import gc
            gc.collect()
            try:
                import torch
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except ImportError:
                pass

    print("\nAll shards written to", RUNS)
    print("Next: python extract_and_score.py")


if __name__ == "__main__":
    main()
