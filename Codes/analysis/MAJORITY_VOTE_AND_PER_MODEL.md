# Majority voting and per-model PASS breakdown

Closes the two remaining analysis-side items from the reviewer comment list
before the writing pass: comment 3 ("3 repetitions + majority voting" applied
literally rather than as paired tests over (probe, seed)), and comment 16
("PASS labels are generous; per-paper PASS typically means at least one of
three models passed").

Both views are computed from the same Phase 4 expanded data already used by
the per-seed paired tests, so the numbers are consistent across views and no
new generation was required.

## Majority voting (reviewer comment 3)

Script: `Codes/analysis/expansion/majority_vote.py`.
Outputs: `Codes/analysis/out/majority_vote.csv` (per-configuration majority
bias rate) and `Codes/analysis/out/majority_vote_tests.csv` (probe-level
paired McNemar tests).

For each (benchmark, model, method, probe), the per-(probe, seed) bias
outcomes from `stats_gen.gen_outcomes` are aggregated by majority vote across
the three seeds into one outcome per probe. Ties (1 vote each, only possible
when a seed is invalid) are broken toward "biased" (conservative). Probes
with zero valid seeds are excluded.

### Headline majority-voted bias rates (the strong signals)

| Benchmark | Model | Method | N probes | Majority bias |
| :-------- | :---- | :----- | :------: | :-----------: |
| IMSB-2025 | DeepSeek | baseline    | 18 | 0.722 |
| IMSB-2025 | DeepSeek | prompt v1   | 18 | 0.778 |
| IMSB-2025 | DeepSeek | prompt v2   | 18 | 0.944 |
| IMSB-2025 | DeepSeek | **AST scrub** | **16** | **0.000** |
| BTM-2025  | DeepSeek | baseline    | 15 | 0.333 |
| BTM-2025  | DeepSeek | **prompt v2** | **15** | **0.000** |
| BU-2024   | Qwen | baseline    | 15 | 0.000 |
| BU-2024   | Qwen | prompt v1   | 15 | 0.333 *(backfire)* |
| UQSB-2023 | all     | all         | 18 | 0.000 |

### Probe-level paired McNemar (the "question-level N" Alessio cited)

Three of 84 comparisons are significant at p < 0.05 under majority voting
(N = 15-18 per comparison). The reduced significance count, relative to the
12 of 84 at the per-(probe, seed) level (N up to 45), is the expected effect
of lower N at the probe level. This is the trade-off the existing
`stats_gen.py` docstring flags: probe-level reporting respects Alessio's
question-level unit but loses power, while per-seed tests gain power by
treating each generation as a sample. **Both views are reported; the per-seed
tests are the primary inferential evidence and the majority-voted view is
reported for unit-of-analysis transparency.**

The three majority-voted significant findings are consistent in direction
with the per-seed analysis: IMSB DeepSeek AST scrubbing dominates prompt
mitigation on stereotype-knowledge bias at the probe level as well.

## Per-model PASS breakdown (reviewer comment 16)

Script: `Codes/analysis/expansion/per_model_pass.py`.
Output: `Codes/analysis/out/per_model_pass.csv`.

Aggregates the paper-scheme threshold-sensitivity rows by (model, mitigation
family) so that the per-model story behind each headline PASS is visible.

| Model              | Family    | Pass | Partial | Fail | Total | Pass fraction |
| :----------------- | :-------- | :--: | :-----: | :--: | :---: | :-----------: |
| CodeGen-350M       | Baseline  |  1   |    0    |  4   |   5   |     0.20      |
| CodeGen-350M       | Prompt    |  2   |    2    |  6   |  10   |     0.20      |
| CodeGen-350M       | AST       |  1   |    1    |  3   |   5   |     0.20      |
| DeepSeek-Coder-1.3B| Baseline  |  2   |    0    |  3   |   5   |     0.40      |
| DeepSeek-Coder-1.3B| Prompt    |  4   |    0    |  6   |  10   |     0.40      |
| DeepSeek-Coder-1.3B| AST       |  3   |    0    |  2   |   5   |     0.60      |
| Qwen2.5-Coder-1.5B | Baseline  |  3   |    0    |  2   |   5   |     0.60      |
| Qwen2.5-Coder-1.5B | Prompt    |  5   |    0    |  5   |  10   |     0.50      |
| Qwen2.5-Coder-1.5B | AST       |  3   |    1    |  1   |   5   |     0.60      |

Across all four methods, CodeGen-350M clears **4 of 20** configurations,
DeepSeek-Coder-1.3B clears **9 of 20**, and Qwen2.5-Coder-1.5B clears
**11 of 20**. The headline per-benchmark PASS verdicts in the Results table
therefore rest on the capable model in each case (DeepSeek for BTM, SEB,
IMSB; Qwen for BU-2024), exactly as reviewer comment 16 anticipated.

## Reframed language

**Results > Statistical tests (extension).**

> Two complementary views are reported. The per-(probe, seed) paired McNemar
> tests in `expanded_tests.csv` (N up to 45, 12 of 84 comparisons significant
> at p < 0.05) treat each generation as a sample, which is valid under
> stochastic decoding. The probe-level majority-voted view in
> `majority_vote_tests.csv` (N 15 to 18, 3 of 84 significant) aggregates the
> three seeds by majority vote into one outcome per probe and matches the
> question-level unit of analysis. Both views agree on the direction of the
> main result (IMSB-2025 post-generation AST scrubbing on DeepSeek-1.3B).

**Results > Per-model breakdown (new paragraph or table).**

> The headline per-benchmark PASS verdicts rely on a capable model in each
> case. Across all 20 (benchmark, method) configurations per model,
> CodeGen-350M clears 4, DeepSeek-Coder-1.3B clears 9, and Qwen2.5-Coder-1.5B
> clears 11 (Table P, `per_model_pass.csv`). Model capacity is a stronger
> determinant of double-gate success than mitigation choice for the weaker
> model: on CodeGen-350M every family clears 1 to 2 of 5 (or 2 to 4 of 10)
> configurations, so a single per-benchmark PASS should not be read as a
> family-wide endorsement on weaker code generators.

## Files

- `Codes/analysis/expansion/majority_vote.py`
- `Codes/analysis/expansion/per_model_pass.py`
- `Codes/analysis/out/majority_vote.csv`
- `Codes/analysis/out/majority_vote_tests.csv`
- `Codes/analysis/out/per_model_pass.csv`
- `Codes/analysis/MAJORITY_VOTE_AND_PER_MODEL.md` - this note.
