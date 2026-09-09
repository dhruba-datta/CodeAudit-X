# Phase 5 — complete full-dataset study

**239,832 generations** across 5 benchmarks × 3 models × 3 methods × 3 seeds on
the full source datasets, plus 6,012 extra BTM-2025 generations (seeds 4–5) so
the authors' @5 metrics can be computed. 319,776 scored pieces after deriving
`postgenast` from the baselines. Zero duplicate job IDs across the three Kaggle
runs. Run provenance (GPU, library versions, model commit SHAs) in
`FULL_RUN_META.json`.

Sources: BTM-2025 and BU-2024 from the authors' released files; UQSB-2023 exact
from the paper's specification; SEB-2023 from HumanEval + MBPP; IMSB-2025 from
CrowS-Pairs. No reconstructions anywhere.

## 1. Scale, against Phase 4

| | Phase 4 (frozen) | Phase 5 (this) | × |
| :-- | --: | --: | --: |
| Probes | 81 | **3,090** | 38 |
| Generations | 4,617 | **239,832** | 52 |
| Distinct probes per benchmark | 15–18 | **334 / 392 / 1138 / 343 / 883** | — |
| Significant McNemar tests | 12 / 84 | **49 / 90** | — |

Every benchmark is now its complete source set and every one clears the
sample-size threshold for the paired tests.

## 2. The stratified sample was already right

The 30% run (shards 0–2) and the full run agree to within ±0.02 on almost every
cell — bias, validity, and pass/fail identical. Stratified sharding delivered a
representative sample at 30%; the remaining 70% tightened the intervals without
moving a single conclusion. That is worth one sentence in the methods section,
because it is the answer to "how would you select a statistically
representative sample?"

## 3. The central claim, at full scale

**31 of 49 significant results involve AST scrubbing.** Baseline → postgenast,
where significant:

| Benchmark | Model | Bias | N | p |
| :-- | :-- | :-- | --: | --: |
| BTM-2025 | CodeGen-350M | 0.333 → **0.000** | 1,024 | ~0 |
| BTM-2025 | DeepSeek-1.3B | 0.195 → **0.000** | 747 | ~0 |
| BTM-2025 | Qwen-1.5B | 0.226 → **0.000** | 733 | ~0 |
| IMSB-2025 | DeepSeek-1.3B | 0.211 → **0.000** | 1,503 | ~0 |
| IMSB-2025 | Qwen-1.5B | 0.122 → **0.000** | 262 | ~0 |
| IMSB-2025 | CodeGen-350M | 0.022 → **0.000** | 323 | 1.6e-02 |
| UQSB-2023 | CodeGen-350M | 0.608 → **0.018** | 1,175 | ~0 |
| UQSB-2023 | Qwen-1.5B | 0.332 → 0.270 | 1,176 | ~0 |

Six cells to exactly zero, N in the hundreds to low thousands. It also beats
both prompt variants significantly on BTM across all three models.

**Scope limitation, stated plainly:** AST scrubbing is a no-op on SEB-2023 and
BU-2024. Those metrics measure consistency across variants, not attribute
usage, so removing attribute references changes nothing. The "most reliable
family" claim holds on three of five benchmarks.

## 4. Prompting backfires — now with seven significant instances

Cases where prompt mitigation made bias significantly *worse* than baseline:

| Benchmark | Model | Variant | Bias | N | p |
| :-- | :-- | :-- | :-- | --: | --: |
| UQSB-2023 | Qwen-1.5B | v2 | 0.332 → **0.563** | 1,176 | ~0 |
| UQSB-2023 | DeepSeek-1.3B | v2 | 0.059 → 0.162 | 512 | ~0 |
| UQSB-2023 | Qwen-1.5B | v1 | 0.336 → 0.392 | 1,157 | 7.8e-03 |
| BU-2024 | CodeGen-350M | v1 | 0.819 → 0.877 | 1,029 | 3.1e-04 |
| BU-2024 | Qwen-1.5B | v2 | 0.822 → 0.874 | 1,020 | 1.1e-03 |
| SEB-2023 | CodeGen-350M | v2 | 0.623 → 0.672 | 1,381 | 4.6e-03 |
| BTM-2025 | CodeGen-350M | v2 | 0.289 → 0.347 | 530 | 4.9e-02 |

Phase 4 had one borderline instance of this. It is now a pattern across four of
five benchmarks.

## 5. The curated subset flattered the models

Double gate: **6 / 60 pass**, against 24 / 60 frozen. Unchanged from the 30%
run. Both gates moved against the models on real data:

- **UQSB-2023** is the defining case. Phase 4 reported ContextBiasRate = 0.000
  for all twelve cells — a benchmark that never fails measures nothing. On the
  paper-exact 392-probe set, baselines run 0.09–0.61 and the benchmark becomes
  informative for the first time.
- **BU-2024** baseline bias went 0.02–0.42 → 0.51–0.82. The 49 reconstructed
  tasks were far easier than the authors' 343.
- **Validity fell** on BTM, SEB and BU — the hand-picked probes were easier to
  answer with parseable code.

This is the "curated, not representative" concern confirmed empirically and in
the direction a reviewer would predict. The reported pass counts change; the
effects sharpen rather than dissolve.

## 6. Known caveats before quoting

- **BU-2024 CodeBiasScore is 0.74–0.89 across the board.** The completion-stub
  scoring bug is fixed (validity 0.10 → 0.87), so this is not that. But the
  metamorphic metric on the authors' 343 tasks has not been independently
  sanity-checked. Verify before presenting BU-2024 as a finding.
- **DeepSeek-1.3B on BU-2024 sits at validity 0.24** while the other two are
  ~0.88. Likely answering in prose. One look at raw outputs would settle it.
- **IMSB-2025 / CodeGen-350M validity ~0.12 is real** — the model returns
  comments, not code. Verified by inspection.
- **Metrics are ours, not the source papers'.** Ferrari has asked for the
  authors' metrics to be adopted alongside. UQSB's classifier and BTM's
  BI@5/BD@5/BE@5 are the first two to implement; the extra BTM seeds exist for
  exactly that.

## Files

- `FULL_all_metrics.csv` — 60-cell double-gate table
- `FULL_expanded_tests.csv` — 90 paired McNemar comparisons
- `FULL_expanded_all_metrics.csv` — per-cell recomputation
- `FULL_RUN_META.json` — environment and model-revision provenance, 3 runs
- `SHARDS_0-2_FINDINGS.md` — the 30% interim, kept for the agreement check

Frozen Phase-4 CSVs under `Codes/analysis/` are untouched.
