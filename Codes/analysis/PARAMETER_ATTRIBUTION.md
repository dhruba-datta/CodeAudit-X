# Parameter attribution: disclosure and reframed claim

This note responds to reviewer comment 8 (parameter attribution). The paper
previously stated that observed differences "are attributable to the model and
mitigation rather than hyperparameters." That claim does not survive an audit
of the actual decoding settings used and must be reframed. The full per-run
hyperparameter table is in `Codes/analysis/out/hyperparameters.csv`.

## What the audit found

Per-benchmark decoding hyperparameters in the paper-reported (Phase 3) runs
were set independently per benchmark, mostly hardcoded in the runner scripts,
and span a wide range. All five reported benchmarks used stochastic decoding
(`do_sample=True`).

| Benchmark | Temperature | max_new_tokens | top_p | seeds |
| :-------- | :---------: | :------------: | :---: | :---: |
| SEB-2023  | 0.2 | 100 | not set | 1-5 |
| BU-2024   | 0.6 | 150 | not set | 1-5 |
| UQSB-2023 | 0.4 | 120 | not set | 1-5 |
| IMSB-2025 | 0.5 | 100 | not set | 1-5 |
| BTM-2025  | 0.4 | 400 | 0.9     | 1-5 |

Spread: temperature 0.2 to 0.6 (3x), max_new_tokens 100 to 400 (4x), top_p set
only on BTM. The probe-expansion sweep (Phase 4) partially standardized but did
not eliminate the variance: BU was reduced from 0.6 to 0.4 and IMSB from 0.5 to
0.4, top_p was set uniformly to 0.9, and max_new_tokens was raised for SEB
(100 to 300) and IMSB (100 to 300). SEB temperature remained at 0.2 in both
phases to match the originating benchmark's structural-consistency setting.

## What the data can and cannot support

- **Valid:** within-benchmark comparisons. For any single benchmark, every
  model and every mitigation was generated under the same decoding settings,
  so the model-vs-model and mitigation-vs-mitigation differences reported
  per benchmark (and the per-dataset paired McNemar tests) are not confounded
  by hyperparameters.
- **Not valid:** cross-benchmark attribution. Statements that compare bias or
  validity across benchmarks (for example, "model X is harder to mitigate on
  benchmark A than on benchmark B") cannot be cleanly attributed to benchmark
  difficulty alone, because temperature, max_new_tokens, and top_p differ.

## Reframed claim language (for the response letter and the paper)

Replace the existing parameter-attribution sentence with the following two
sentences in the Results introduction and add the disclosure paragraph to
Threats to Validity.

**Results (replacement sentence).**
Within each benchmark every (model, mitigation) configuration was generated
under identical decoding settings (Table H, `hyperparameters.csv`), so the
within-benchmark model and mitigation comparisons we report are not
confounded by hyperparameters. We do not make cross-benchmark attribution
claims and report results per dataset.

**Threats to Validity (new paragraph).**
Decoding hyperparameters were inherited from the originating benchmark
scripts and therefore differ across the five reported datasets (temperature
in the range 0.2 to 0.6, `max_new_tokens` in the range 100 to 400, `top_p`
set only on BTM). The probe-expansion sweep partially standardized these
settings (Section X, Table H) but did not eliminate the variance. We
mitigate this threat by (i) holding hyperparameters constant within each
benchmark across models and mitigations, (ii) reporting results per dataset
rather than pooled across datasets, and (iii) disclosing every value in
`Codes/analysis/out/hyperparameters.csv`. A future revision could standardize
the decoding settings across benchmarks, but that would require regenerating
every run and is outside the scope of this revision.

## Response-letter excerpt (point-by-point reply)

> **Comment 8 (parameter attribution).** Hyperparameters varied across
> benchmarks, which undermines the claim that observed differences are
> attributable to model and mitigation rather than decoding settings.
>
> **Response.** We accept this point. The full per-benchmark decoding settings
> are now disclosed in Table H (`Codes/analysis/out/hyperparameters.csv`):
> temperature 0.2 to 0.6, `max_new_tokens` 100 to 400, `top_p` set only on
> BTM. We have rephrased the original claim to limit it to within-benchmark
> comparisons (where decoding settings are constant across models and
> mitigations) and added a Threats-to-Validity paragraph documenting the
> cross-benchmark variance. The probe-expansion sweep partially standardized
> these settings without re-running the original results.

## Files

- `Codes/analysis/out/hyperparameters.csv` - authoritative per-benchmark
  per-phase table with source-file citations.
- `Codes/analysis/PARAMETER_ATTRIBUTION.md` - this note.
