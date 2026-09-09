#!/usr/bin/env python3
"""
CodeAudit-X full run: extraction, AST scrubbing, and scoring.

Turns the JSONL generation shards from run_full.py into the exact on-disk
layout the frozen Phase-4 analysis stack already reads:

    runs_clean/<benchmark>_<model>_<method>_expanded/ast_extract/*.json

so that afterwards you run the EXISTING scripts, unmodified:

    cd ../analysis/expansion
    python analyze_expansion.py     --runs ../../fullrun/runs_clean
    python threshold_sensitivity.py --runs ../../fullrun/runs_clean
    python majority_vote.py         --runs ../../fullrun/runs_clean
    python per_model_pass.py        --runs ../../fullrun/runs_clean

That reuse is deliberate. The full run must not introduce a second, subtly
different implementation of the metrics -- if the numbers move, it has to be
because the data changed, not because the scorer did.

Every reusable piece is imported from the frozen Phase-4 code:
    reextract.robust_clean   prefix truncation + validity gate
    reextract.reextract_one  per-benchmark AST extraction
    apply_scrub.scrub        the five postgenast transforms

postgenast is derived here from the baseline generations. It requires no GPU
and no new generation -- which is also the repo-level proof that no method in
this study modifies weights or logits.

Usage:
  python extract_and_score.py                      # everything in runs/
  python extract_and_score.py --benchmark BTM-2025
  python extract_and_score.py --no-scrub           # skip postgenast derivation
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from prompts import clean_code  # noqa: E402
from uqsb_values import uses_demographic_value  # noqa: E402
from config import (BENCHMARKS, BIAS_GATE, GEN_METHODS, MODELS, OUT, RUNS,  # noqa: E402
                    SEEDS, UTILITY_GATE)

EXPANSION = HERE.parents[0] / "analysis" / "expansion"
ANALYSIS = HERE.parents[0] / "analysis"
sys.path.insert(0, str(EXPANSION))
sys.path.insert(0, str(ANALYSIS))

import reextract as RX          # noqa: E402  robust_clean, reextract_one
import apply_scrub as AS        # noqa: E402  scrub
import reanalyze as RA          # noqa: E402  ADAPTERS (load_*, agg_*, bias key)

CLEAN = HERE / "runs_clean"

# Probe fields each benchmark's extractor needs, mapped out of the JSONL record.
PROBE_MAP = {
    "SEB-2023":  lambda p: {"task_id": p.get("task_id"), "variant_id": p.get("variant")},
    "BU-2024":   lambda p: {"task_id": p.get("id"), "variant_id": p.get("variant")},
    "UQSB-2023": lambda p: {"probe_id": p.get("probe_id"), "attribute": p.get("attribute")},
    "IMSB-2025": lambda p: {"task_id": p.get("id"), "object": p.get("object")},
    "BTM-2025":  lambda p: {"prompt_id": p.get("prompt_id")},
}

SAFE = re.compile(r"[^A-Za-z0-9._-]+")

# Completion-style benchmarks: the prompt ends MID-FUNCTION (the signature is in
# the prompt) and the model returns only the body. Two things go wrong if the
# raw output is scored as-is:
#
#   1. Without the signature the validity gate sees a bare indented block, finds
#      no `def`, and scores every CORRECT answer invalid. Measured on BU-2024 /
#      qwen1.5b baseline (shards 0-2, n=766): validity 0.103 -> 0.867.
#   2. The model usually keeps going after the body and emits further, unrelated
#      functions (BU-2024: 10-51% of outputs; UQSB-2023: nearly all, because its
#      prompt is a few-shot list of functions). clean_code() then picks the FIRST
#      `def` in the raw text, which is one of those hallucinated functions, not
#      the target. On UQSB-2023 the study's `code` field was the target function
#      in 0-4 of 1,176 records per model (Phase 5, 9 Sept 2026). Phase 4 was not
#      affected: its curated prompts had no trailing signature, so the model
#      wrote the `def` itself.
#
# Rule: scored code = signature + body, truncated at the next top-level
# definition, then robust_clean. The prefix is per benchmark; UQSB's signature
# differs per probe so it is read off the probe's prompt.
def _uqsb_prefix(probe):
    lines = [l for l in (probe.get("prompt") or "").splitlines() if l.strip()]
    sig = lines[-1] if lines and lines[-1].lstrip().startswith("def ") else ""
    return sig + "\n" if sig else ""


COMPLETION_PREFIX = {
    "BU-2024":   lambda probe: "def is_suitable(obj):\n    ",
    "UQSB-2023": _uqsb_prefix,
}


def completion_code(benchmark, rec):
    """The code to score for one generation record."""
    raw = rec.get("raw") or rec.get("code") or ""
    make_prefix = COMPLETION_PREFIX.get(benchmark)
    if make_prefix is None:
        return RX.robust_clean(rec.get("code") or raw)
    prefix = make_prefix(rec.get("probe") or {})
    if not prefix:                       # probe lacks a signature: fall back
        return RX.robust_clean(rec.get("code") or raw)
    body = raw.lstrip("\n")
    if not body.startswith((" ", "\t")) and prefix.endswith("\n"):
        body = "    " + body            # model dropped the indentation
    return RX.robust_clean(clean_code(prefix + body))


def run_dir(benchmark, model, method):
    d = CLEAN / f"{benchmark}_{model}_{method}_expanded" / "ast_extract"
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_extraction(benchmark, model, method, rec, code):
    """Extract with the frozen Phase-4 extractor and persist one JSON piece."""
    old = dict(PROBE_MAP[benchmark](rec.get("probe") or {}))
    old["seed"] = rec["seed"]
    old["method"] = method
    ext = RX.reextract_one(benchmark, code, old)
    if benchmark == "UQSB-2023":
        # Under the paper-exact prompts "attribute appears in a condition" is
        # ~1.00 everywhere (see uqsb_values.py). Keep that figure under a new
        # name and make the value-aware rule the one every downstream loader
        # reads, so the McNemar tests and the gate are on the meaningful metric.
        ext["uses_sensitive_in_logic_any"] = ext.get("uses_sensitive_in_logic", False)
        ext["uses_demographic_value"] = uses_demographic_value(code)
        ext["uses_sensitive_in_logic"] = ext["uses_demographic_value"]
    ext["seed"] = rec["seed"]
    ext["method"] = method
    ext["model"] = model
    ext["job_id"] = rec["job_id"]
    fname = SAFE.sub("_", f"{rec['job_id']}__{method}") + ".json"
    (run_dir(benchmark, model, method) / fname).write_text(json.dumps(ext))
    return ext


def iter_shards(benchmarks):
    for bm in benchmarks:
        for path in sorted((RUNS / bm).glob("*.jsonl")) if (RUNS / bm).is_dir() else []:
            yield bm, path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", action="append", choices=BENCHMARKS)
    ap.add_argument("--no-scrub", action="store_true",
                    help="do not derive the postgenast cells from baseline")
    ap.add_argument("--metrics-only", action="store_true",
                    help="skip extraction; recompute the metrics table from runs_clean/ "
                         "(use after extracting benchmark by benchmark)")
    args = ap.parse_args()
    benchmarks = args.benchmark or BENCHMARKS

    OUT.mkdir(parents=True, exist_ok=True)
    counts = defaultdict(int)

    for bm, path in ([] if args.metrics_only else iter_shards(benchmarks)):
        with path.open() as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    counts[f"{bm}|torn-lines"] += 1
                    continue
                model, method = rec["model"], rec["method"]
                code = completion_code(bm, rec)
                write_extraction(bm, model, method, rec, code)
                counts[f"{bm}|{model}|{method}"] += 1

                # postgenast, derived inline from the baseline piece. Done here
                # rather than in a second pass so we never hold ~60k generations
                # in memory at full scale.
                if method == "baseline" and not args.no_scrub:
                    old = dict(PROBE_MAP[bm](rec.get("probe") or {}))
                    scrubbed = AS.scrub(bm, code, old)
                    write_extraction(bm, model, "postgenast", rec,
                                     RX.robust_clean(scrubbed))
                    counts[f"{bm}|{model}|postgenast"] += 1
        print(f"[extract] {path.name}")

    # ---- recompute the headline metrics per cell ---------------------------
    rows = []
    for bm in benchmarks:
        load, agg, bias_key = RA.ADAPTERS[bm]
        if bm == "UQSB-2023":
            _agg = agg
            def agg(pieces, _agg=_agg):
                a = _agg(pieces)
                a["DemographicValueRate"] = a.pop("ContextBiasRate")
                return a
            bias_key = "DemographicValueRate"
        for model in MODELS:
            for method in GEN_METHODS + (["postgenast"] if not args.no_scrub else []):
                ext = CLEAN / f"{bm}_{model}_{method}_expanded" / "ast_extract"
                if not ext.is_dir():
                    continue
                pieces = load(str(ext))
                if not pieces:
                    continue
                a = agg(pieces)
                validity = a.get("ValidityRate")
                bias = a.get(bias_key)
                gate_bias = (isinstance(bias, (int, float)) and bias <= BIAS_GATE[bm])
                gate_util = (isinstance(validity, (int, float)) and validity >= UTILITY_GATE[bm])
                rows.append({
                    "benchmark": bm, "model": model, "method": method,
                    "n_pieces": len(pieces),
                    "ValidityRate": validity,
                    "bias_metric": bias_key, "bias": bias,
                    "bias_gate": BIAS_GATE[bm], "utility_gate": UTILITY_GATE[bm],
                    "pass_bias": int(gate_bias), "pass_utility": int(gate_util),
                    "PASS": int(gate_bias and gate_util),
                })

    if not rows:
        sys.exit("No extractions found. Did run_full.py write anything to runs/ ?")

    import csv
    metrics_csv = OUT / "full_all_metrics.csv"
    with metrics_csv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    passes = sum(r["PASS"] for r in rows)
    print(f"\nExtracted {sum(counts.values()):,} pieces into {CLEAN}")
    print(f"Metrics   -> {metrics_csv}")
    print(f"Double gate: {passes}/{len(rows)} cells pass both gates")
    print("\nNext (existing Phase-4 scripts, unmodified):")
    print("  cd ../analysis/expansion")
    for s in ("analyze_expansion.py", "threshold_sensitivity.py",
              "majority_vote.py", "per_model_pass.py"):
        print(f"  python {s} --runs {CLEAN}")


if __name__ == "__main__":
    main()
