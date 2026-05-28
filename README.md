# CodeAudit-X

CodeAudit-X is a framework and open repository for identifying, quantifying, and
mitigating social bias in code-generating large language models (LLMs). It
consolidates probes and metrics from peer-reviewed code-bias benchmarks into a
single orchestration pipeline and evaluates every mitigation under a double-gate
criterion that scores fairness and code utility jointly.

This repository accompanies the paper *CodeAudit-X: A Multi-Benchmark Study of
Social Bias Mitigation in Code-Generating Large Language Models*.

Literature review, experimental parameters, and cross-paper comparisons are
maintained in the [CodeAudit X - Master Research Sheet](https://docs.google.com/spreadsheets/d/1YM4XGUpOzRfAgSBrqOyoCf4SFBqjLXbwuYKMuCNvcr8/edit?usp=sharing).

## Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Methodology](#methodology)
- [Results](#results)
- [Reproducibility](#reproducibility)
- [Reviewed Literature](#reviewed-literature)
- [Getting Started](#getting-started)

## Overview

LLM-generated code increasingly drives socio-technical decisions in domains such
as hiring, lending, and insurance, where biased logic that still compiles and
passes tests can cause real allocational harm. CodeAudit-X addresses two gaps in
prior work: code-bias benchmarks are usually run in isolation with
heterogeneous metrics, and general LLM-fairness frameworks rarely reason about
executable code and fairness together. The framework provides:

- a model-agnostic probe library derived from peer-reviewed code-bias
  benchmarks;
- a shared metric layer (bias and utility) with a double-gate controller;
- three mitigation families: prompt engineering, post-generation Abstract
  Syntax Tree (AST) scrubbing, and a model-editing proxy;
- a run registry and per-benchmark comparison records that make every reported
  result traceable.

**Reported scope.** Five peer-reviewed benchmarks are reported in the paper:
BTM-2025, UQSB-2023, SEB-2023, BU-2024, and IMSB-2025. FC-2025 and MGB-2024 are
arXiv preprints; they were implemented and run in the same pipeline for
completeness but are excluded from the paper's reported results.

## Repository Structure

```text
CodeAudit-X/
├── README.md                     # This document
└── Codes/
    ├── notebooks/                # Baseline-replication notebooks (one per benchmark)
    ├── prompts/                  # Structured JSON probes and bias-sensitive templates
    ├── notes/                    # Per-benchmark methodology and lifecycle notes
    ├── outputs/                  # Run manifests, per-paper metrics, structure spec
    ├── requirements.txt          # Python dependencies
    ├── mitigation/               # Phase 3 mitigation pipeline
    │   ├── scripts/              # Runner and post-generation scripts (per benchmark)
    │   ├── configs/              # Experiment configurations (per benchmark)
    │   ├── comparisons/          # Per-benchmark final-status and comparison JSONs
    │   ├── RUN_REGISTRY.csv      # Canonical index of every registered run
    │   └── README.md             # Mitigation pipeline documentation
    └── analysis/                 # Phase 4 re-analysis and probe-expansion study
        ├── reanalyze.py          # Per-piece reconstruction, validated against frozen metrics
        ├── stats.py              # Question-level paired tests
        ├── stats_gen.py          # Generation-level paired (McNemar) tests
        ├── PARAMETER_ATTRIBUTION.md  # Per-benchmark decoding-settings disclosure
        ├── THRESHOLD_SENSITIVITY.md  # Validity-floor and bias-gate sensitivity
        ├── REANALYSIS_SUMMARY.md     # Phase 4 summary
        ├── out/                  # Per-piece tables, sensitivity sweeps, hyperparameters
        └── expansion/            # Expanded-probe sweep (3 models, 3 seeds)
            ├── probes/           # Expanded probe library (15 to 18 probes per benchmark)
            ├── run_expansion.py  # Resumable generation runner
            ├── reextract.py      # Robust AST re-extraction (prefix truncation, validity gate)
            ├── apply_scrub.py    # Post-generation AST scrubbing on expanded baselines
            ├── analyze_expansion.py     # Consolidated metrics and significance tests
            ├── threshold_sensitivity.py # Double-gate threshold sweep
            └── out/              # Expanded metrics and per-dataset test results
```

The raw per-run output folders (per-seed generations and AST extracts) and the
third-party reference PDFs are produced or held locally and are intentionally
not committed; the reviewed papers are cited, with DOIs, in the paper's
bibliography. Reviewers work from the run registry, the comparison JSONs, and
the manifests.

## Methodology

The study proceeds in four phases.

### Phase 1: Probe Design

Bias scenarios drawn from a curated review of 21 papers are encoded as
reusable, model-agnostic JSON probes. Each probe specifies the protected
attributes, the input/output schema, and the invariances expected of unbiased
code. The review is curated rather than systematic and is not treated as a
separate study phase; the probes are derived from prior work.

### Phase 2: Baseline Replication

The benchmarks are replicated in a shared Python 3.11 orchestration environment
using CodeGen-350M-mono as the reference model, re-implementing each
benchmark's own metric to establish baseline bias and code validity.

### Phase 3: Mitigation and Comparison

Mitigation methods are applied across three open-weight models
(CodeGen-350M-mono, Qwen2.5-Coder-1.5B-Instruct, DeepSeek-Coder-1.3B-Instruct).
Every run is scored and passed through the double-gate controller:

- **Fairness Gate**: the benchmark's bias metric must fall below its
  task-specific threshold (inherited from the source benchmark).
- **Utility Gate**: `ValidityRate` must exceed a per-benchmark floor
  (0.8 for BTM-2025; 0.5 for the other four). The choice is robust: a
  sensitivity sweep (`Codes/analysis/out/threshold_sensitivity_summary.csv`)
  shows the total pass-count moves by at most two of 60 configurations
  across any uniform floor in [0.3, 0.8].

A configuration is successful only if it clears both gates.

### Phase 4: Re-analysis and probe expansion

Phase 4 (`Codes/analysis/`) recomputes the double-gate verdicts from the
per-piece generations and addresses the unit-of-analysis, statistical-rigor,
and probe-size concerns raised in review. The probe sets are expanded from
3-4 to 15-18 distinct probes per benchmark, the three-model sweep is
regenerated at three seeds under stochastic decoding, and a robust
re-extraction step strips trailing natural-language explanations and applies
a parseable-function validity gate (correcting a previously-hidden artifact
that disproportionately penalized the more instruction-tuned models).
Post-generation AST scrubbing is then re-applied to the expanded baselines so
the prompt-engineering and AST-scrubbing families can be compared at scale,
with per-dataset paired McNemar tests. Threshold sensitivity, per-benchmark
hyperparameter disclosure, and the corrected per-dataset numbers all draw
from this phase.

## Results

All bias and validity values are recomputed from the per-piece outputs of
the Phase 4 expanded probe sweep
(`Codes/analysis/expansion/out/expanded_all_metrics.csv`, 60 configurations
covering 5 benchmarks x 3 models x 4 methods). The double-gate verdicts use
the per-benchmark fairness gates and the paper's validity-floor scheme
(BTM 0.8, the other four 0.5). "Baseline" is the unmitigated reference run
for each model.

**Statistical tests.** Per-dataset paired McNemar tests over (probe, seed)
pairs are reported in
`Codes/analysis/expansion/out/expanded_tests.csv`: 12 of 84 paired
comparisons are significant at p < 0.05, including all three of
(baseline vs AST scrubbing), (AST vs prompt v1), and (AST vs prompt v2) on
IMSB-2025 / DeepSeek-1.3B.

### Peer-reviewed benchmarks (reported)

| Benchmark | Bias metric | Best configuration | Bias (baseline to best) | ValidityRate | Gate (bias / validity) | Test | Outcome |
| :-------- | :---------- | :----------------- | :---------------------- | :----------: | :--------------------- | :--- | :-----: |
| BTM-2025  | CodeLevelProtectedUsageRate | DeepSeek-1.3B, prompt v2     | 0.30 to 0.00 | 0.91 | ≤ 0.1 / ≥ 0.8 | p ≈ 0.001 | Pass |
| UQSB-2023 | ContextBiasRate             | all configurations           | 0.00 to 0.00 | 1.00 | ≤ 0.2 / ≥ 0.5 | n/a       | Pass |
| SEB-2023  | PerturbationBiasRate        | DeepSeek-1.3B, prompt v1     | 0.27 to 0.18 | 0.94 | ≤ 0.3 / ≥ 0.5 | n.s.      | Pass |
| BU-2024   | CodeBiasScore               | Qwen-1.5B, baseline          | 0.02 (already below gate) | 1.00 | ≤ 0.2 / ≥ 0.5 | n/a   | Pass |
| IMSB-2025 | BiasKnowledgeRate           | DeepSeek-1.3B, AST scrubbing | 0.69 to 0.00 | 0.50 | ≤ 0.1 / ≥ 0.5 | p < 0.001 | Pass |

Each of the five benchmarks is cleared by at least one capable model. The
strongest single result is IMSB-2025: post-generation AST scrubbing on
DeepSeek-1.3B reduces stereotype-knowledge bias from 0.69 to 0.00 (paired
McNemar p ≈ 5e-4) and significantly beats prompt mitigation on the same
probes (p < 1e-4). Prompt mitigation is the only family that drives BTM
DeepSeek to bias 0.00, and prompt v1 is significantly preferred over v2 on
SEB DeepSeek (p ≈ 0.008).

### Mitigation families (peer-reviewed benchmarks, paper-scheme thresholds)

| Mitigation family             | Pass both gates | Partial (bias only) | Fail / no valid output |
| :---------------------------- | :-------------: | :-----------------: | :--------------------: |
| Baseline (reference)          |        6        |          0          |            9           |
| Prompt engineering            |       11        |          2          |           17           |
| Post-generation AST scrubbing |        7        |          2          |            6           |

Post-generation AST scrubbing is the most reliable family per configuration
(7 of 15 clear both gates vs 11 of 30 for prompt engineering) and is the
only family that meaningfully reduces stereotype-knowledge bias on IMSB-2025.
Prompt engineering wins decisively where it suits the benchmark (BTM-2025
DeepSeek-1.3B prompt v2 to bias 0.00, p ≈ 0.001) but can backfire on
benchmarks whose baselines are already clean (BU-2024 Qwen-1.5B: prompt v1
raises bias from 0.02 to 0.27, p ≈ 0.003), supporting a per-context choice
rather than a single universal mitigation. The model-editing proxy is a
gender-pronoun rewriter specific to MGB-2024 and is not a third family for
the five reported benchmarks (Threats to Validity).

### arXiv preprints (excluded from reported results)

FC-2025 (FairCoder) and MGB-2024 were implemented and run for completeness.
Their per-benchmark records are available under
`Codes/mitigation/comparisons/` but are excluded from the paper's reported
results because the source papers are not peer-reviewed.

## Reproducibility

- `Codes/mitigation/RUN_REGISTRY.csv` is the canonical index. Each row links a
  `(benchmark, model, method, seed)` configuration to its config file, output
  location, and computed metrics.
- `Codes/mitigation/comparisons/<BENCHMARK>/<BENCHMARK>_pilot_final_status.json`
  is the authoritative verdict per benchmark, including the pass criteria.
- `Codes/outputs/STRUCTURE.md` documents the output layout and naming
  conventions. Per-paper manifests and metrics are under
  `Codes/outputs/<BENCHMARK>/`.
- All paths in the registry are repository-relative. The raw per-seed
  generations and AST extracts are regenerated locally and are not committed.
- `Codes/analysis/expansion/out/expanded_all_metrics.csv` is the consolidated
  per-piece results table from Phase 4 (3 models x 5 benchmarks x 4 methods);
  `Codes/analysis/expansion/out/expanded_tests.csv` carries the per-dataset
  paired McNemar tests; `Codes/analysis/out/` holds the threshold sensitivity
  sweep and the per-benchmark hyperparameter disclosure.

## Reviewed Literature

The 21 reviewed papers (peer-reviewed code-bias and LLM-fairness work plus
provider/multilingual studies) are cited with DOIs or arXiv identifiers in the
paper's bibliography. The reference PDFs are not redistributed in this
repository.

## Getting Started

1. **Environment.** Python 3.9 or later.
2. **Dependencies.** `pip install -r Codes/requirements.txt` (the Phase 3
   mitigation pipeline additionally uses
   `Codes/mitigation/requirements_phase3.txt`).
3. **Baselines.** Run any notebook in `Codes/notebooks/` to replicate a
   benchmark's baseline.
4. **Mitigation.** See `Codes/mitigation/README.md` for the Phase 3 pipeline.
5. **Re-analysis.** See `Codes/analysis/` for the per-piece re-analysis and the
   expanded-probe sweep.
