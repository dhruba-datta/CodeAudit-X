# Phase 5, shards 0–2 — first real full-dataset results

70,929 generations. A stratified 30% sample of the full study (shards 0, 1, 2 of
10), across 5 benchmarks × 3 models × 4 methods × 3 seeds. Shards 3–9 are
running; these numbers will be superseded, not contradicted, when they land.

Sources: BTM-2025 and BU-2024 from the authors' released files, UQSB-2023 exact
from the paper's specification, SEB-2023 from HumanEval + MBPP, IMSB-2025 from
CrowS-Pairs. No reconstructions.

## 1. Statistical power — the thing Ferrari asked for

| | Phase 4 (frozen) | Phase 5 shards 0–2 |
| :-- | --: | --: |
| Distinct probes per benchmark | 15–18 | **102 / 105 / 117 / 266 / 344** |
| Significant McNemar tests | 12 / 84 | **34 / 90** |
| Sample-size warning | "still small" | **"OK for tests"** on all five |

Every benchmark now clears the tool's own sample-size threshold. That alone
answers the unit-of-analysis objection.

## 2. The headline claim survives at scale, and hardens

**24 of the 34 significant results involve AST scrubbing.** It is now the
dominant effect in the study rather than one good result on one benchmark.

AST scrubbing drives bias to exactly 0.000, significantly, on:

| Benchmark | Model | baseline → postgenast | N | p |
| :-- | :-- | :-- | --: | --: |
| BTM-2025 | CodeGen-350M | 0.426 → 0.000 | 197 | ~0 |
| BTM-2025 | DeepSeek-1.3B | 0.181 → 0.000 | 138 | ~0 |
| BTM-2025 | Qwen-1.5B | 0.201 → 0.000 | 134 | ~0 |
| IMSB-2025 | DeepSeek-1.3B | 0.206 → 0.000 | 433 | ~0 |
| IMSB-2025 | Qwen-1.5B | 0.087 → 0.000 | 80 | 1.6e-02 |
| UQSB-2023 | CodeGen-350M | 0.601 → 0.020 | 351 | ~0 |

and beats **both** prompt variants significantly on BTM across all three models.

**Prompt mitigation backfires, significantly.** UQSB-2023 / Qwen-1.5B:
baseline 0.328 → promptmit_v2 **0.593** (p ~ 0, N=351). The "prompting can make
it worse" claim was one borderline result in Phase 4; it is now unambiguous.

## 3. The curated subset was flattering the models

Double gate: **6/60 cells pass, against 24/60 frozen.** Both gates moved against
the models, on real data:

- **Bias is higher.** UQSB-2023 is the clearest case. Phase 4 reported
  ContextBiasRate = 0.000 for *all twelve* cells — a benchmark on which nothing
  ever fails is measuring nothing. On the paper-exact 392-probe set, baselines
  run 0.085–0.601. UQSB becomes an informative benchmark for the first time.
- **Validity is lower.** The hand-picked probes were easier to answer with
  parseable code than the authors' real task sets.

This is the "curated, not statistically representative" concern, confirmed
empirically and in the direction a reviewer would predict. It is a finding, not
a failure — but the paper's reported pass counts will change.

## 4. A bug this run exposed — read before quoting any BU-2024 number

BU-2024 prompts are **completion stubs**: `def is_suitable(obj):` sits in the
prompt and the model returns only the body. The validity gate looked for a `def`
in the output, never found one, and scored **every correct answer invalid**.

Measured on BU-2024 / Qwen-1.5B baseline, n=766:

| | ValidityRate |
| :-- | --: |
| as originally scored | 0.103 |
| with the signature restored | **0.867** |

Fixed in `extract_and_score.py` (`COMPLETION_PREFIX`). All numbers in this
document are post-fix. UQSB-2023 is also completion-style but carries decoy
functions ahead of the signature, so its outputs already parse — deliberately
left alone rather than risk pulling the decoys into the bias metric.

## 5. What still needs checking

- **BU-2024 CodeBiasScore is 0.74–0.89 across the board.** Validity is now
  healthy, so this is not the same bug — but the metamorphic metric on the
  authors' 343 real tasks has not been independently sanity-checked. Do not
  present BU-2024 as a finding until it has been.
- **DeepSeek on BU-2024 sits at validity 0.240** while CodeGen and Qwen are near
  0.88. Worth one look at its raw outputs; DeepSeek tends to answer in prose.
- **IMSB / CodeGen-350M validity ~0.11 is real**, not a bug — the model returns
  comments rather than code. Verified by inspection.

## Files

- `full_all_metrics.csv` — 60-cell double-gate table
- `full_expanded_tests.csv` — 90 paired McNemar comparisons
- `full_expanded_all_metrics.csv` — per-cell recomputation

Frozen Phase-4 CSVs under `Codes/analysis/` are untouched and remain the cited
numbers until the full run completes.
