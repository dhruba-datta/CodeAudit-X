# Launching the full-dataset run

## The size of the thing

```
$ python run_full.py --plan
BTM-2025    334 probes x 3 methods x 3 seeds x 3 models =   9,018
UQSB-2023   392 probes x 3 x 3 x 3                      =  10,584
SEB-2023   1138 tasks x 4 variants x 3 x 3 x 3          = 122,904
BU-2024      49 tasks x 8 variants x 3 x 3 x 3          =  10,584
IMSB-2025  1000 triplets x 3 x 3 x 3                    =  27,000
                                                   TOTAL  180,090
```

`postgenast` adds **zero** generations — it is a deterministic AST scrub of the
baseline outputs, derived afterwards by `extract_and_score.py`. That is also the
cleanest answer to Ferrari's "do your methods modify weights or logits?": the
fourth method needs no model at all.

SEB-2023 is 68% of the bill because HumanEval + MBPP is 1138 tasks and every
task is rendered in 4 perturbation variants. If you need a cheaper first run,
`--benchmark` everything except SEB costs ~57k generations, then add SEB.

---

## Read this first: it can be free

**Kaggle gives 30 GPU-hours per week at no cost, and this study needs 5–10.**
The whole thing fits in one week's quota. See [KAGGLE.md](KAGGLE.md).

The rest of this document covers paid options, which are worth it if you want
the run finished in an afternoon rather than across a few sessions.

## Reality check on the free Hugging Face tier

You said you'd run this on Hugging Face. The free tier will not do it, and it's
better to know that before you burn a week finding out.

| Option | What you get | Verdict for a 180k-generation sweep |
| :-- | :-- | :-- |
| **Free Space, CPU Basic** | 2 vCPU, 16 GB RAM, no GPU | No. CodeGen-350M on CPU is seconds per generation; this is months. |
| **Free ZeroGPU** | H200 slice, **~3.5 minutes of GPU time per day**, resets 24 h after first use; free accounts in good standing may host up to 2 ZeroGPU Spaces | No. Also the wrong shape — ZeroGPU allocates in short bursts for interactive demos, not long batch jobs, and vLLM doesn't fit that model. |
| **PRO ZeroGPU** ($9/mo) | 8× the quota (~25–28 min/day), priority queue, pre-paid credits beyond quota; overage $1 per 10 min | Technically possible over many days, but you'd be paying overage rates to do batch work on interactive hardware. Don't. |
| **HF Jobs** | Container on a GPU flavour, billed **per minute**, only while Starting or Running | **Yes — this is the right HF product.** It is a batch job, which is what this is. |
| **Space with paid GPU hardware** | Same hardware menu, but a long-lived app you must remember to pause | Works, but Jobs bills only while running and stops on its own. Prefer Jobs. |
| **RunPod / Vast.ai RTX 4090** | ~$0.20–0.40/hr | Yes — the §7 plan from your meeting prep, and still cheapest per hour. |

**Jobs does not strictly require PRO.** The docs say Jobs are available to any
user or organization *with a positive credit balance*. A PRO subscription
includes monthly compute credits that count toward that balance, which is why
PRO is the usual route — but the gate is credit, not the subscription.

### Flavour pricing (from the Jobs pricing page)

| Flavour | GPU memory | $/hr | Note |
| :-- | --: | --: | :-- |
| Nvidia T4 – small | 16 GB | 0.40 | Cheapest GPU. fp16 only — pass `--dtype half`. |
| **1× Nvidia L4** | **24 GB** | **0.80** | **Best value for 350M–1.5B models. Start here.** |
| Nvidia A10G – small | 24 GB | 1.00 | |
| 1× Nvidia L40S | 48 GB | 1.80 | Overkill at this model size. |
| Nvidia A100 – large | 80 GB | 2.50 | |
| Nvidia H200 | 141 GB | 5.00 | Fastest, but you're paying for memory you can't use. |

An L4 fits all three models comfortably and should land the full 180k
generations in roughly 5–10 hours — call it **$4–8 for the entire study**, and
**well under $1 for one shard of ten**. Confirm with the pilot before committing;
`hf jobs hardware` prints the live list.

**The default Jobs timeout is 30 minutes.** A full run will be killed mid-way
unless you pass `--timeout`. Use `--timeout 3h` per shard and let resumability
handle the rest.

Pricing and quota move; re-check
[Jobs pricing](https://huggingface.co/docs/hub/jobs-pricing) and
[ZeroGPU docs](https://huggingface.co/docs/hub/en/spaces-zerogpu) before you commit.

---

## Breaking it into pieces (recommended)

You do not have to run 180,090 generations in one sitting, and you probably
shouldn't. `--shards N` splits every benchmark's probe set into N chunks:

```bash
python run_full.py --shards 10 --shard-report     # see the split, run nothing
python run_full.py --shards 10 --shard 0 --plan   # 17,955 generations, ~10%
python run_full.py --shards 10 --shard 0 --backend vllm
```

**Each shard is a stratified sample of the whole, not a contiguous slice.** The
probe sets are built by crossing dimensions, so a contiguous block would be
systematically skewed — shard 0 of UQSB-2023 would be nothing but `ethnicity`.
Instead every shard gets a proportional share of every stratum (protected
attribute, task template, HumanEval vs MBPP), verified to within one probe:

```
UQSB-2023  (392 probes, 10 shards, stratified by attribute)
  shard    age  disability  ethnicity  gender  nationality  race  religion  total
      0      6           5          5       5            5     6         6     38
      1      6           6          5       5            5     5         6     38
  ...
  partition OK: 0 duplicates, 0 missing, max stratum deviation 0.6
```

That property is what makes this worth doing. **Stop after any number of shards
and what you hold is a statistically representative subsample of the full
benchmark** — which is a real answer to "why only a subset?", unlike the
hand-curated 15–18. One shard of ten is ~18k generations and already gives you
roughly 33 of BTM's 48 decision tasks and every protected attribute in UQSB.

Shards accumulate into the same files, so this:

```bash
python run_full.py --shards 10 --shard 0 --backend vllm   # Monday
python run_full.py --shards 10 --shard 1 --backend vllm   # Tuesday
```

leaves exactly the same data on disk as running both at once. Re-running a
completed shard is a no-op. `runs/RUN_META.json` keeps the full history of
which shards were generated when, so provenance survives a stop-start run
spread over weeks.

Two rules: don't change `--shards N` partway through (it repartitions
everything and orphans what's on disk), and don't change `SHARD_SEED` in
`sharding.py` for the same reason.

## Step 0 — the pilot (do this first)

Ferrari suggested a one-hour trial. This is it. It measures throughput on real
hardware so the full-run cost becomes a number you can defend.

```bash
git clone <your repo> && cd CodeAudit-X/Codes/fullrun
pip install -r requirements-gpu.txt
python build_full_probes.py                 # pulls HumanEval, MBPP, CrowS-Pairs
python run_full.py --backend vllm --limit 20 --model qwen1.5b
```

The runner prints `gen/s` per batch. Multiply out:

```
full_run_hours = 180090 / (gen_per_second * 3600)
```

Do it once per model — CodeGen-350M will be several times faster than Qwen-1.5B,
so a single average understates the cheap end.

## Step 1 — the full run

```bash
python build_full_probes.py
python run_full.py --backend vllm
python extract_and_score.py
./run_phase4_analysis.sh
```

Every stage is resumable. `run_full.py` skips any `job_id` already present in a
shard, so a killed spot instance costs you the current batch and nothing else.
Just re-run the same command.

### On HF Jobs

```bash
hf auth login
hf jobs hardware            # confirm the flavour names and live prices

hf jobs run \
  --flavor l4x1 \
  --timeout 3h \
  --secrets HF_TOKEN \
  --image vllm/vllm-openai:latest \
  -- bash -c '
      git clone https://huggingface.co/datasets/dhruba-datta/codeaudit-x /work &&
      cd /work/Codes/fullrun &&
      pip install -r requirements-gpu.txt &&
      python build_full_probes.py &&
      python run_full.py --backend vllm --shards 10 --shard 0 &&
      python extract_and_score.py &&
      hf upload dhruba-datta/codeaudit-x-fullrun ./runs ./runs_clean --repo-type dataset
  '
```

Three things that will cost you a run if you skip them:

- **`--timeout`.** The default is 30 minutes. Without it the job dies partway
  through and you pay for the wasted minutes.
- **Upload before exit.** The container filesystem does not survive. Push
  `runs/` to a dataset repo — that is also what makes the next shard resumable,
  since `run_full.py` skips job_ids it finds there.
- **Verify the flavour name** with `hf jobs hardware`. The CLI's flag names have
  moved around between releases; check `hf jobs run --help` too.

One shard per job is the natural unit: ~18k generations, comfortably inside a
3-hour timeout, under a dollar, and it leaves you with a representative sample
even if you stop there.

### On RunPod / a plain GPU box

Same four commands. Put the repo on the network volume, not the container disk,
so a restart resumes instead of starting over.

## Step 2 — check it against the frozen numbers

Before you tell anyone the full-set results differ from the paper, prove the
difference is the data and not the pipeline:

```bash
python run_full.py --backend vllm --legacy-decoding --limit 18
```

`--limit 18` on legacy decoding approximates the Phase-4 curated pilots. The
metrics should land near `Codes/analysis/expansion/out/expanded_all_metrics.csv`.
If they don't, something in the environment changed and the full-set numbers are
not yet trustworthy.

---

## Source datasets — verified on the Hub, Aug 2026

| Benchmark | Source | Status |
| :-- | :-- | :-- |
| SEB-2023 | `openai/openai_humaneval` (164) | parquet, viewer works |
| SEB-2023 | `google-research-datasets/mbpp`, config `full` (974) | parquet, viewer works. **974 spans four splits** — `train+test+validation+prompt`. Omitting `prompt` silently loses 10 tasks. |
| IMSB-2025 | CrowS-Pairs (1508) | **the canonical repo is broken** — see below |

`nyu-mll/crows_pairs` contains only a loading script and no data file at all,
and its own Hub page says the viewer is disabled because the repo "requires
arbitrary Python code execution". `datasets` 3.x dropped script-based datasets,
so `load_dataset("nyu-mll/crows_pairs")` fails outright.

`build_full_probes.py` therefore reads a parquet/CSV mirror and **verifies it**
against the canonical 1508 rows and the `sent_more` / `sent_less` / `bias_type`
schema before accepting it. A mirror that doesn't match is rejected, not used.
If every mirror fails, download `crows_pairs_anonymized.csv` from the authors'
repo (`github.com/nyu-mll/crows-pairs`, `data/`) and drop it at
`Codes/fullrun/sources/crows_pairs_anonymized.csv` — that path is checked first.

Source-dataset failures abort the build. They do not fall back to a duplicated
curated set, because the failure mode that matters here is quietly reporting
1000 copies of 18 probes as if they were CrowS-Pairs.

## Two things that will bite you

**1. The Phase-4 analysis scripts overwrite the frozen CSVs.**
`analyze_expansion.py`, `threshold_sensitivity.py`, `majority_vote.py` and
`per_model_pass.py` honour `--runs` for input but hard-code their output to
`Codes/analysis/expansion/out/` and `Codes/analysis/out/` — the CSVs the current
30-page draft cites. Always go through `./run_phase4_analysis.sh`, which stashes
them, runs the analysis, files the results under `fullrun/out/full_*.csv`, and
puts the frozen ones back.

**2. Disk and inodes.**
`extract_and_score.py` writes one small JSON per generation, matching the layout
the Phase-4 loaders expect. At full scale that's ~180k baseline pieces plus
~180k scrubbed pieces. Budget ~50 GB and a filesystem that doesn't mind the
inode count, or run benchmark-by-benchmark and archive `runs_clean/` between
passes.
