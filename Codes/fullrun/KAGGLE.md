# Running the full study free on Kaggle

Kaggle gives **30 GPU-hours per week, free, no credit card**. The full 180,090
generations need roughly 5–10 GPU-hours. The entire study fits inside one week's
quota with room to spare, and you can redo it next week if you break something.

This is the cheapest correct answer, and it's better than the free Hugging Face
tier by two orders of magnitude (ZeroGPU gives ~3.5 minutes a day).

| | Kaggle free | Colab free | HF ZeroGPU free |
| :-- | :-- | :-- | :-- |
| Quota | **30 h/week, guaranteed** | 15–30 h/week, throttled | ~3.5 min/day |
| Hardware | 2×T4 (32 GB) or P100 | T4, availability varies | H200 slice, burst only |
| Session | up to 9–12 h | 12 h, disconnects | seconds per call |
| Background run | **yes — close the tab** | no | no |
| Enough for this study | **yes** | maybe, with babysitting | no |

## The split that makes this work

Only **generation** needs a GPU. Extraction, AST scrubbing, the metrics and
every statistical test are pure CPU work on text you already have.

So: generate on Kaggle, score on your Mac.

```
Kaggle (GPU)                          your M4 (CPU)
  build_full_probes.py                  extract_and_score.py
  run_full.py  -> runs/*.jsonl   --->   run_phase4_analysis.sh
```

That split also dodges Kaggle's output-size limit. The JSONL shards are ~270 MB
for the whole study; `runs_clean/` — the ~360k one-file-per-generation tree the
Phase-4 loaders want — is tens of GB and would blow the notebook output cap.
Never build it on Kaggle.

## Budget honestly before you start

180,090 generations is about 45M output tokens. A T4 is bandwidth-poor
(320 GB/s) and under vLLM a 1.5B model realistically runs somewhere between 800
and 2,500 output tokens/sec — a wide enough band to matter:

| | optimistic | pessimistic |
| :-- | --: | --: |
| Qwen2.5-Coder-1.5B | 5 h | 15 h |
| DeepSeek-Coder-1.3B | 4.5 h | 14 h |
| CodeGen-350M | 1.5 h | 5 h |
| **Total on one T4** | **~11 h** | **~34 h** |

At the good end that's a third of the weekly quota. At the bad end it exceeds
it and spills into a second week. **Run the pilot in Cell 2 first** — it turns
this range into one measured number in about two minutes.

### Use both T4s — it is free

An hour on the `T4 ×2` accelerator costs **one** hour of quota, not two. vLLM
uses one GPU by default, so the second sits idle unless you ask for it. Run two
models concurrently and wall-clock halves at no extra quota cost:

```python
import subprocess
jobs = []
for gpu, model in enumerate(["qwen1.5b", "deepseek1.3b"]):
    env = {**os.environ, "CUDA_VISIBLE_DEVICES": str(gpu)}
    jobs.append(subprocess.Popen(
        ["python", "run_full.py", "--backend", "vllm", "--dtype", "half",
         "--gpu-mem", "0.85", "--model", model, "--shards", "10", "--shard", "0"],
        env=env))
for j in jobs:
    j.wait()
```

One model per GPU, not tensor parallelism — these models are far too small for
TP to pay off, and separate processes keep the shards independent. Drop
`--gpu-mem` to 0.85 since you are no longer alone on the box.

## Setup (once)

1. **Verify your phone** on Kaggle. Internet access in notebooks is off until
   you do, and without it you cannot pip install or pull models.
2. Push this repo somewhere the notebook can clone it (a public GitHub repo, or
   upload `Codes/fullrun/` as a Kaggle Dataset).
3. New Notebook → Settings → **Accelerator: GPU T4 ×2**, **Internet: On**,
   **Persistence: Files only**.

## The notebook

Cell 1 — setup:

```python
!pip install -q vllm datasets transformers
!git clone -q https://github.com/<you>/CodeAudit-X /kaggle/working/repo
%cd /kaggle/working/repo/Codes/fullrun
!python build_full_probes.py
```

Cell 2 — a short pilot, so you measure throughput before spending quota:

```python
!python run_full.py --backend vllm --dtype half \
    --model qwen1.5b --benchmark BTM-2025 --limit 20
```

`--dtype half` is not optional. T4 and P100 predate bf16, and vLLM's `auto`
will fail on them.

Read the `gen/s` it prints, then:

```
hours_for_full_study = 180090 / (gen_per_second * 3600)
```

Cell 3 — one shard (~18k generations, comfortably inside a session):

```python
!python run_full.py --backend vllm --dtype half --shards 10 --shard 0
```

Cell 4 — package the output for download:

```python
!cd /kaggle/working/repo/Codes/fullrun && tar czf /kaggle/working/shard0.tar.gz runs/
```

Then **Save Version → Save & Run All (Commit)**. This runs in the background —
close the tab, come back later. Download `shard0.tar.gz` from the output, or
better, save `runs/` as a Kaggle Dataset and attach it to the next notebook so
the next shard resumes instead of regenerating.

## Then on your Mac

```bash
tar xzf shard0.tar.gz -C Codes/fullrun/
cd Codes/fullrun
python extract_and_score.py
./run_phase4_analysis.sh
```

No GPU needed, and no quota consumed.

## Working through the shards

A session caps at 9–12 hours, so shard-per-session is the natural rhythm.
Because shards are stratified, stopping at any point leaves you with a
representative sample rather than a partial one — see the README.

Attach the previous run's `runs/` as an input dataset and copy it into place
before generating, so `run_full.py` skips what's already done:

```python
!mkdir -p runs && cp -r /kaggle/input/codeaudit-runs/* runs/ 2>/dev/null || true
!python run_full.py --backend vllm --dtype half --shards 10 --shard 1
```

## Things that will cost you a session

- **`--dtype half`.** Forget it and vLLM dies on T4 at model load.
- **Internet off.** Silent-ish failure at pip install; check Settings.
- **Building `runs_clean/` on Kaggle.** Tens of GB, hits the output cap. Do
  extraction on your Mac.
- **Committing without saving `runs/`.** Interactive session files vanish. Save
  a Version or write to a Dataset.
- **`gpu_memory_utilization`.** The default 0.90 is fine on a dedicated T4, but
  if you hit OOM pass `--gpu-mem 0.80`.
- **Leaving the second T4 idle.** It costs the same quota either way. See the
  dual-GPU cell above.
- **Re-downloading the models every session.** Three models is ~9 GB and eats
  quota as wall-clock. After the first session, save the HF cache as a Kaggle
  Dataset and attach it:
  `!mkdir -p ~/.cache/huggingface && cp -r /kaggle/input/hf-cache/* ~/.cache/huggingface/`

## Splitting shards across different platforms

You can run shard 0 on Kaggle, shard 1 on Colab and shard 2 on a rented GPU.
The design supports it, and here is precisely why it stays valid.

Identical seeds do **not** guarantee identical output across different GPUs,
vLLM builds or dtypes — floating-point reduction order differs, so a T4 and an
A100 can diverge on the same prompt and seed. That would be fatal if it landed
between two things you compare. It doesn't:

- sharding is at **probe** level, so a probe never splits across shards;
- every method, seed and variant of a probe lives in the same shard;
- the paired McNemar tests compare methods **within** a (probe, seed).

So every comparison you actually report ran on one machine. Hardware variation
can shift absolute rates slightly between shards; it cannot bias the paired
comparisons, which is where the claims live.

Two conditions:

1. **Never split one shard across platforms.** Finish a shard where you started
   it, or discard and redo it. Half a shard on a T4 and half on an A100 puts
   the confound inside a probe group, which is exactly what the design avoids.
2. **Report the mix.** `runs/RUN_META.json` records, per invocation, the GPU
   names, torch/vLLM versions, dtype, and the resolved commit SHA of every
   model. If a Hub repo is updated between sessions the SHA changes and you
   will see it — otherwise two shards a month apart could silently use
   different weights.

If you do split, say so in the paper in one line: which shards ran on what, and
that the paired analysis is within-shard by construction. That is a strength,
not an admission.

## Other free options, ranked

1. **Kaggle** — 30 h/week guaranteed, background execution. Use this.
2. **Colab Pro** ($9.99/mo, NOT included in Google AI Pro — checked) — 100
   compute units/month. A T4 burns roughly 1.2–1.8 CU/hr, so 100 CU is on the
   order of 55–80 T4-hours, carrying over for 90 days. Unlocks **L4 and A100**
   at 2–5× a T4; CU burn scales roughly with speed, so the faster card costs
   about the same per generation and finishes far sooner. Only worth buying if
   Kaggle's 30 h/week proves too slow.
3. **Lightning AI** — persistent workspace, free monthly credits (~22 h on a
   T4). Worth it if you hate re-installing vLLM every session, since the
   environment survives.
4. **Colab free** — same hardware, less quota, no background execution, throttled
   when busy. Fine as overflow; Kaggle and Colab together are ~60 h/week.
5. **Modal** — free monthly credits, per-second billing, but you'd rewrite the
   runner as Modal functions. Not worth it here.
6. **Google Cloud credits from a Google AI Pro subscription** — as of Jan 2026
   Google folded Developer Program premium into AI Pro, which now carries
   **$10/month in GCP credits** (Ultra: $100). That is ~12 h on an on-demand L4
   or ~35 h on spot, so it would cover this study. The catch is friction: new
   GCP projects have GPU quota set to **zero** and need a quota-increase request
   that can take days, plus VM setup and spot preemption. Keep as a backstop for
   hitting the Kaggle wall mid-week, not as the primary route.
7. **HF ZeroGPU free** — 3.5 min/day. Not viable, see LAUNCH.md.

Note on Gemini / Google AI Studio: irrelevant here. This study runs specific
open-weight models (CodeGen-350M, Qwen2.5-Coder-1.5B, DeepSeek-Coder-1.3B)
whose exact weights are the object of measurement. An API to a different model
cannot substitute.

Quotas move. Re-check before you plan around them.
