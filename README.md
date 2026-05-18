# CodeAudit-X

CodeAudit-X is a framework and open repository for identifying, quantifying, and
mitigating social bias in code-generating large language models (LLMs). It
consolidates probes and metrics from peer-reviewed code-bias benchmarks into a
single orchestration pipeline and evaluates every mitigation under a double-gate
criterion that scores fairness and code utility jointly.

This repository accompanies the paper *CodeAudit-X: A Multi-Benchmark Study of
Social Bias Mitigation in Code-Generating Large Language Models*.

## Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Methodology](#methodology)
- [Results](#results)
- [Reproducibility](#reproducibility)
- [Reviewed Literature](#reviewed-literature)
- [Getting Started](#getting-started)
- [Research Tracking](#research-tracking)

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
    └── mitigation/               # Phase 3 mitigation pipeline
        ├── scripts/              # Runner and post-generation scripts (per benchmark)
        ├── configs/              # Experiment configurations (per benchmark)
        ├── comparisons/          # Per-benchmark final-status and comparison JSONs
        ├── RUN_REGISTRY.csv      # Canonical index of every registered run
        └── README.md             # Mitigation pipeline documentation
```

The raw per-run output folders (per-seed generations and AST extracts) and the
third-party reference PDFs are produced or held locally and are intentionally
not committed; the reviewed papers are cited, with DOIs, in the paper's
bibliography. Reviewers work from the run registry, the comparison JSONs, and
the manifests.

## Methodology

The study proceeds in three phases.

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
- **Utility Gate**: `ValidityRate` must exceed an empirically set floor
  (0.5 in general; 0.8 for benchmarks whose baseline already exceeds 0.8).

A configuration is successful only if it clears both gates.

## Results

All values are taken from the per-benchmark final-status records in
`Codes/mitigation/comparisons/`. "Baseline" is the unmitigated reference model.

### Peer-reviewed benchmarks (reported)

| Benchmark | Bias metric | Best configuration | Bias (baseline to best) | ValidityRate | Gate (bias / validity) | Outcome |
| :-------- | :---------- | :----------------- | :---------------------- | :----------: | :--------------------- | :-----: |
| BTM-2025  | CodeLevelProtectedUsageRate | DeepSeek-1.3B, prompt v2 + post-gen AST | 1.0 to 0.0 | 0.867 | ≤ 0.1 / ≥ 0.8 | Pass |
| UQSB-2023 | ContextBiasRate             | DeepSeek-1.3B, prompt v1                | high to 0.0 | 0.933 | ≤ 0.2 / ≥ 0.5 | Pass |
| SEB-2023  | PerturbationBiasRate        | Qwen-1.5B, prompt v1                    | high to 0.231 | 0.55 | ≤ 0.3 / ≥ 0.5 | Pass |
| BU-2024   | CodeBiasScore               | Qwen-1.5B, post-gen AST                 | high to 0.0 | 1.00 | ≤ 0.2 / ≥ 0.5 | Pass |
| IMSB-2025 | BiasKnowledgeRate           | post-gen AST (all three models)         | 1.0 to 0.0 | 1.00 | ≤ 0.1 / ≥ 0.5 | Pass |

Each benchmark is cleared by at least one capable model. Model capacity matters
independently of the mitigation family: on BU-2024 the same post-generation
pipeline passes on Qwen-1.5B but leaves residual bias on the weaker models.

### Mitigation families (peer-reviewed benchmarks, all runs)

| Mitigation family       | Pass both gates | Partial (bias only) | Fail / no valid output |
| :---------------------- | :-------------: | :-----------------: | :--------------------: |
| Prompt engineering      |        2        |          5          |           22           |
| Post-generation AST     |        8        |          2          |            6           |

Post-generation AST scrubbing is the most reliable family; prompt engineering
helps on contextual and perturbation bias with capable models but frequently
trades code utility for fairness. The model-editing proxy was applied only to
the excluded MGB-2024 benchmark.

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

## Reviewed Literature

The 21 reviewed papers (peer-reviewed code-bias and LLM-fairness work plus
provider/multilingual studies) are cited with DOIs or arXiv identifiers in the
paper's bibliography. The reference PDFs are not redistributed in this
repository.

## Getting Started

1. **Environment.** Python 3.11 or later.
2. **Dependencies.** `pip install -r Codes/mitigation/requirements_phase3.txt`
3. **Baselines.** Run any notebook in `Codes/notebooks/` to replicate a
   benchmark's baseline.
4. **Mitigation.** See `Codes/mitigation/README.md` for the Phase 3 pipeline.

## Research Tracking

Literature review, experimental parameters, and cross-paper comparisons are
maintained in the master tracking sheet:
<https://docs.google.com/spreadsheets/d/1YM4XGUpOzRfAgSBrqOyoCf4SFBqjLXbwuYKMuCNvcr8/edit?usp=sharing>
