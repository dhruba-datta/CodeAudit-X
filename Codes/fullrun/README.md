# Phase 5 — Full-dataset run

This directory answers the single biggest open review item: the paper's results
come from **15–18 hand-curated probes per benchmark**, and the reviewer asked
why. This pipeline runs the same grid over the **full source datasets** with
**one standardized decoding configuration**, so the answer stops being "curated,
not statistically representative" and becomes a number.

Nothing here replaces Phase 4. The frozen Phase-4 artifacts stay exactly where
they are and stay quotable; this produces a parallel set under `out/full_*.csv`.

## What changes vs Phase 4

| | Phase 4 (frozen) | Phase 5 (here) |
| :-- | :-- | :-- |
| Probes | 15–18 curated per benchmark | full source sets (334 / 392 / 1138 / 343 / 1000) |
| Generations | ~7k | ~180k |
| Decoding | per-benchmark (temp 0.2–0.6, tokens 100–400) | one setting for all five |
| Cross-benchmark claims | not permitted | defensible |
| Metrics / extraction / scrub code | — | **identical, imported from Phase 4** |

That last row matters. `extract_and_score.py` imports `reextract.robust_clean`,
`reextract.reextract_one` and `apply_scrub.scrub` from
`Codes/analysis/expansion/`, and writes into the exact directory layout the
Phase-4 analysis scripts already read. If the full-set numbers move, it is
because the data changed, not because a second scorer was written.

## Files

| File | Role |
| :-- | :-- |
| `config.py` | the whole grid: models, decoding, gates, targets. Nothing else hard-codes these. |
| `build_full_probes.py` | builds the full-size probe sets → `probes_full/` |
| `prompts.py` | prompt construction, lifted verbatim from `run_expansion.py::iter_jobs` |
| `sharding.py` | splits each probe set into N **stratified** chunks that can be run separately |
| `run_full.py` | generation. vLLM / transformers / stub backends. Resumable, shardable. |
| `extract_and_score.py` | AST extraction + postgenast derivation + double-gate metrics |
| `run_phase4_analysis.sh` | runs the four Phase-4 scripts **without clobbering the frozen CSVs** |
| `KAGGLE.md` | **how to run the whole study free** on Kaggle's 30 GPU-h/week |
| `LAUNCH.md` | paid options (HF Jobs, RunPod) with flavour pricing, if you want it done fast |

## Quick start

```bash
pip install -r requirements-gpu.txt
python build_full_probes.py          # needs network for HumanEval/MBPP/CrowS-Pairs
python run_full.py --plan            # see the size before you pay for it
python run_full.py --backend vllm
python extract_and_score.py
./run_phase4_analysis.sh
```

No GPU? `python run_full.py --backend stub --limit 3` exercises the entire chain
with placeholder code in about a second. It proves the plumbing; **its numbers
are meaningless** and must never be reported.

## Running it in pieces

180k generations does not have to happen in one sitting.

```bash
python run_full.py --shards 10 --shard-report      # inspect the split
python run_full.py --shards 10 --shard 0 --plan    # 17,955 generations
python run_full.py --shards 10 --shard 0 --backend vllm
```

Each shard is a **stratified** sample of the whole — every shard holds a
proportional share of every protected attribute, task template and source
dataset, verified to within one probe. A contiguous slice would not: shard 0 of
UQSB-2023 would be entirely `ethnicity`.

The consequence is the point. Stopping after k of N shards leaves a
statistically representative subsample of the full benchmark, so a partial run
is publishable rather than merely incomplete — the concession §8 of the meeting
prep anticipated, obtained for free. Shards are disjoint and accumulate into the
same files, so running shard 0 on Monday and shard 1 on Tuesday is
byte-equivalent to running both at once, and `runs/RUN_META.json` records the
whole invocation history.

Sharding happens at probe level, never at generation level: every method, seed
and variant of a probe stays together, because SEB-2023 and BU-2024 measure bias
by comparing variants of one probe against each other and the McNemar tests pair
methods on the same (probe, seed). Splitting a probe across shards would
silently destroy both.

Do not change `--shards N` or `SHARD_SEED` partway through a run — either
repartitions everything and orphans what is already on disk.

## Probe provenance — read before quoting anything

`probes_full/MANIFEST.json` records a `provenance` value per benchmark. Four
levels, in descending authority:

| Level | Benchmark | Source |
| :-- | :-- | :-- |
| `official-authors-release` | **BTM-2025** (334) | [`huangd1999/CBS`](https://github.com/huangd1999/CBS) `dataset/dataset.json`, Apache-2.0, pinned commit |
| `official-authors-release` | **BU-2024** (343) | [`janeeyre912/fairness_testing_code_generation`](https://github.com/janeeyre912/fairness_testing_code_generation) `dataset/tasks.json`, AAAI-25 artifact |
| `paper-exact` | **UQSB-2023** (392) | one template × 49 modifiers × 8 dimensions, all reproduced verbatim from the paper |
| `official-source-datasets` | SEB-2023 (1138) | HumanEval + MBPP from the Hub — **but see the warning** |
| `official-source-datasets` | IMSB-2025 (1000) | CrowS-Pairs, verified mirror — **but see the warning** |
| `reconstructed` | `--offline` only | combinatorial stand-in. **Never report these numbers.** |

Three of the five now use the authors' own material. BTM and BU are fetched at
build time rather than vendored — BU's repo carries **no license**, so it is
usable but not redistributable. UQSB's repo ships the bias classifier and its
training corpus but not the prompts; the paper specifies them completely
(one template, 49 modifiers, 8 dimensions), so this is exact, not approximate.

### Two warnings that affect the paper, not just this code

**SEB-2023 does not introduce a "Code of Many Colors" dataset.** The word
"color" does not appear in [the paper](https://aclanthology.org/2023.findings-acl.718/)
(arXiv:2211.00609). There is no 8-domain, 1000-prompt corpus. It applies prompt
perturbations to HumanEval, MBPP and DeepMind Code Contests. More seriously, the
biases it measures are **cognitive** — keyword reliance, function-name
memorisation — not **social**. Citing it as a social-bias benchmark
misrepresents it, and the project's literature table currently does.

**IMSB-2025 is not a code benchmark.** [Chen et al.](https://aclanthology.org/2025.findings-naacl.39/)
(arXiv:2408.11843) edit bias knowledge in BERT and GPT-2; there is no code
generation in the paper at all. It also does not use BiasNLI, which the
literature table claims. Its own artifact was never released, so only the
upstream CrowS-Pairs and StereoSet corpora are reusable.

Both need resolving before submission — either by re-describing them accurately
as what they are, or by replacing them.

## Known gotcha

The Phase-4 analysis scripts write to fixed output directories regardless of
`--runs`, and would overwrite the CSVs the current draft cites. Use
`./run_phase4_analysis.sh`, never the scripts directly.
