# CodeAudit-X Re-analysis Summary (Phase 4 revision, May 2026)

Addresses Alessio's review demands on unit of analysis, statistics, "small
numbers", and "all metrics for all datasets". **No model inference was used** —
everything below is recomputed from the per-probe x per-seed generations already
on disk. Scripts: `Codes/analysis/reanalyze.py` (load + validate + per-piece
table), `stats.py` (question-level), `stats_gen.py` (generation-level tests).
Outputs in `Codes/analysis/out/`.

## 1. Validation against frozen results (trust check)
Recomputed every run's aggregate from the per-piece data and compared to the
frozen `*_metrics.json`. **49 runs, 1,635 code pieces.**
- BU-2024, IMSB-2025, SEB-2023, UQSB-2023: **exact match** on ValidityRate and
  the bias metric for every run.
- BTM-2025: ValidityRate matches exactly; bias counts match exactly. The only
  divergence is a denominator convention (frozen BTM CLPUR = biased/total;
  all other benchmarks = biased/valid). Standardised here to biased/valid.

## 2. KEY FINDING — the real cause of the "small numbers"
The unit of analysis can be reported three ways; the sample size per dataset is:

| Benchmark | Distinct questions (probes) | Generations (probe x seed) per config |
|---|---|---|
| BTM-2025  | 3 | 15 |
| UQSB-2023 | 3 | 15 |
| SEB-2023  | 3 tasks (x4 framings) | 15 metamorphic groups |
| BU-2024   | 3 tasks (x4 variants) | 15 metamorphic groups |
| IMSB-2025 | 4 triplets | 20 |

**At the question level every benchmark has only 3-4 questions.** No statistical
test can be significant on N=3-4. This is the root cause of "8 of 16 / 2 of 29"
and cannot be fixed by re-analysis alone — it requires expanding the probe sets
(more questions), which needs new generation runs.

## 3. Statistics that ARE possible now (generation level, no runs)
Treating each generation (probe x seed) as the sample (valid for stochastic
decoding, `do_sample=True`, seeds 1-5) and pairing two techniques on the same
(probe, seed), McNemar's exact test gives:
- **IMSB-2025: post-gen AST scrubbing vs prompt mitigation is significant for
  all three models** (bias 0.0 vs 1.0; 20/20 discordant; p < 1e-5). Structural
  scrubbing removes stereotype-knowledge bias that prompting leaves at 100%.
- Elsewhere the direction is consistent (scrubbing <= prompting on bias) but
  **not significant**: discordant counts are small and low validity shrinks the
  paired sample (e.g. Qwen/BU has 1 shared valid generation). 6 of 38
  comparisons significant, all IMSB postgen-vs-prompt.

Question-level Wilcoxon/McNemar (N=3-4) are all non-significant by construction
and should be reported only as "underpowered; see probe-expansion plan".

## 4. Data-integrity issues found (fix before submission)
- **BTM-2025 was run with an inconsistent protocol**: three different extraction
  schemas across runs (`ast_sensitive_usage`, `metrics`, `refined_metrics`); a
  duplicate codegen `promptmit_v1` run; and codegen v1(190130)/v2/v3 have 30
  pieces (6 prompt phrasings) while every other run has 15 (3). The frozen BTM
  aggregates were therefore computed by different scripts with different
  denominators. Recommend re-running BTM under one clean protocol.
- **CLPUR denominator** differs from the other benchmarks' bias rates
  (total vs valid). Standardise and state the formula.
- **No Qwen / DeepSeek baselines exist** — baselines were only run for
  CodeGen-350M. So "mitigation reduces bias vs no mitigation" cannot be shown
  for the two stronger models; only mitigation-vs-mitigation comparisons are
  possible for them. Generating these baselines needs runs (no probe design).
- **Decoding temperature varies by benchmark** (0.2-0.6, some hard-coded in
  scripts). Constant within a benchmark, so per-dataset analysis is clean, but
  the cross-benchmark aggregate claim must be dropped and per-benchmark
  temperature disclosed.

## 5. Artifacts (in Codes/analysis/out/)
- `per_piece_long.csv` — 1,635 rows: benchmark, model, method, probe, seed, valid, biased.
- `validation_vs_frozen.csv` — recomputed vs frozen, per run.
- `all_metrics_all_datasets.csv` — every metric for every (benchmark, model, method).
- `pairwise_tests.csv` — question-level tests (underpowered).
- `pairwise_tests_generation.csv` — generation-level McNemar tests.

## 6. Still to do
- No runs: threshold sensitivity sweep on the validity floor (0.5/0.8);
  extend the model-edit proxy (output rewriter) to the 5 benchmarks for a real
  RQ3 three-way comparison; formal indicator/formula table; per-case bias examples.
- Needs runs: Qwen+DeepSeek baselines (5 benchmarks); probe-set expansion to
  ~15-30 questions/benchmark for question-level statistical power; optional
  large API LLM to address the small-model critique and raise validity.
