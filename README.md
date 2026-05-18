# CodeAudit X

**CodeAudit X** is a research initiative focused on identifying, quantifying, and mitigating social biases in Large Language Models (LLMs) specialized for code generation. The project replicates and extends state-of-the-art methodologies to evaluate fairness across various domains, including banking, healthcare, and software engineering.

---

## 📊 Research Tracking

All literature reviews, experimental parameters, and cross-paper comparisons are maintained in the master tracking sheet:
**[CodeAudit X - Master Research Sheet](https://docs.google.com/spreadsheets/d/1YM4XGUpOzRfAgSBrqOyoCf4SFBqjLXbwuYKMuCNvcr8/edit?usp=sharing)**

---

## 📁 Repository Structure

```text
CodeAudit X/
├── PHASE_STATUS.md       # Comprehensive phase tracker
└── Codes/
    ├── notebooks/        # Jupyter Notebooks for each paper replication
    ├── prompts/          # Structured JSON probes and bias-sensitive templates
    ├── outputs/          # Run manifests, structure spec, and per-paper indices
    ├── notes/            # Markdown logs and execution summaries
    └── mitigation/       # Phase 3 mitigation experiments
        ├── scripts/      # Runner & postgen scripts (per paper)
        ├── configs/      # Experiment configurations (per paper)
        ├── comparisons/  # Per-paper final-status & comparison JSONs
        ├── CHANGELOG_PHASE3.md
        ├── RUN_REGISTRY.csv
        └── README.md     # Pipeline documentation
```

> **Repository scope.** The raw per-run output folders (the thousands of
> per-seed generations and AST extracts) are produced locally and are *not*
> shipped in this public repository; reviewers work from the run registry,
> the per-paper comparison JSONs, and the manifests instead. The 21 reviewed
> papers are not redistributed here; they are cited (with DOIs) in the paper's
> bibliography.
>
> **Reported set.** Five benchmarks are peer-reviewed and reported in the
> paper: **BTM-2025, UQSB-2023, SEB-2023, BU-2024, IMSB-2025**. **FC-2025**
> and **MGB-2024** are arXiv preprints (not peer-reviewed); they were
> implemented and run in the same pipeline but are excluded from the paper's
> reported results and appear below only as work performed.

---

## 🔄 Research Pipeline

### Phase 1 — Probe Design ✅

Reviewed 21 papers on LLM code-generation bias (cited in the paper's bibliography), and defined structured JSON probes per domain.

### Phase 2 — Baseline Replications ✅

Replicated all 7 implemented benchmarks to establish baseline bias measurements using `codegen-350M` (5 peer-reviewed + the 2 arXiv preprints, FC-2025 and MGB-2024, kept for completeness).

| Paper         | Domain            | Methodology                            | Status |
| :------------ | :---------------- | :------------------------------------- | :----: |
| **BTM-2025**  | Income Prediction | Sensitive token usage via AST Visitors |   ✅   |
| **FC-2025**   | Software Pipeline | Few-shot Scoring Logic Fairness        |   ✅   |
| **IMSB-2025** | Knowledge Storage | Triplet-based Bias Probes              |   ✅   |
| **MGB-2024**  | Model Editing     | Profession-Gender Association          |   ✅   |
| **BU-2024**   | Metamorphic Flow  | Metamorphic Solar framework            |   ✅   |
| **UQSB-2023** | Social Logic      | Contextual Attribute Encoding          |   ✅   |
| **SEB-2023**  | Model Stability   | Prompt Perturbation Analysis           |   ✅   |

**Locked**: 2026-02-19 (Tag: `phase2-complete`)

### Phase 3 — Mitigation (7 pilots run; 5 peer-reviewed reported) ✅

Prompt-level and post-generation mitigation to reduce bias while maintaining code validity. The five peer-reviewed pilots below are the ones reported in the paper; FC-2025 and MGB-2024 are shown as completed work but are excluded from the paper's reported results (not peer-reviewed).

#### BTM-2025 Pilot — ✅ PASSED

| Model             | Method                  | Validity  |  Bias   |  Gate  |
| :---------------- | :---------------------- | :-------: | :-----: | :----: |
| CodeGen-350M      | Prompt v2               |   0.40    |   0.0   |   ❌   |
| Qwen-1.5B         | Prompt v1               |   0.60    |   0.0   |   ❌   |
| DeepSeek-1.3B     | Prompt v1 + PostGen     |   0.733   |   0.0   |   ❌   |
| **DeepSeek-1.3B** | **Prompt v2 + PostGen** | **0.867** | **0.0** | **✅** |

**Winning pipeline**: `deepseek-coder-1.3b-instruct` + v2 prompt + post-gen AST scrub\
**Gates**: `ValidityRate ≥ 0.8` · `CodeLevelProtectedUsageRate ≤ 0.1`\
**Frozen**: 2026-02-19

#### FC-2025 Pilot — ✅ PASSED *(arXiv preprint — not peer-reviewed; excluded from the paper's reported results)*

Task-based evaluation with FC-specific metrics (RefusalRate, PreferenceEntropy, FairScore).

| Task                    | Best Model       | FairScore | ValidityRate | Gate |
| :---------------------- | :--------------- | :-------: | :----------: | :--: |
| Function Implementation | **Qwen-1.5B**    |  **1.0**  |   **1.0**    |  ✅  |
| Test Case Generation    | **CodeGen-350M** |  **1.0**  |   **0.5**    |  ✅  |

**Gates**: `FairScore ≥ 0.7` · `ValidityRate ≥ 0.5`\
**Models**: CodeGen-350M (PASS), Qwen-1.5B (PASS), DeepSeek-1.3B (FAIL)\
**Runs**: 18 canonical · **Frozen**: 2026-02-20

See [`Codes/mitigation/README.md`](Codes/mitigation/README.md) for full pipeline docs.

#### UQSB-2023 Pilot — ✅ PASSED

Context injection probes for social bias leakage in code logic.

| Model             | Best Method   | ContextBiasRate | ValidityRate | Verdict |
| :---------------- | :------------ | :-------------: | :----------: | :-----: |
| **DeepSeek-1.3B** | **prompt v1** |     **0.0**     |  **0.933**   | ✅ PASS |
| **CodeGen-350M**  | **postgen**   |     **0.0**     |   **0.6**    | ✅ PASS |
| Qwen-1.5B         | —             |       NA        |     0.0      |   NA    |

**Gates**: `ContextBiasRate ≤ 0.2` · `ValidityRate ≥ 0.5`\
**Runs**: 9 canonical · **Frozen**: 2026-02-20

#### SEB-2023 Pilot — ✅ PASSED

Prompt perturbation stability auditing.

| Model             | Best Method   | PerturbationBiasRate | ValidityRate | Verdict |
| :---------------- | :------------ | :------------------: | :----------: | :-----: |
| **Qwen-1.5B**     | **prompt v1** |      **0.2308**      |   **0.55**   | ✅ PASS |
| **DeepSeek-1.3B** | **prompt v2** |       **0.0**        |   **0.4**    | PARTIAL |
| **CodeGen-350M**  | **prompt v2** |       **0.25**       |  **0.2833**  | PARTIAL |

**Gates**: `PerturbationBiasRate ≤ 0.3` · `ValidityRate ≥ 0.5`\
**Runs**: 18 canonical · **Frozen**: 2026-02-20

#### BU-2024 Pilot — ✅ PASSED

Metamorphic flow bias auditing (Solar framework).

| Model             | Best Method    | CodeBiasScore | ValidityRate | Verdict |
| :---------------- | :------------- | :-----------: | :----------: | :-----: |
| **Qwen-1.5B**     | **postgen v1** |    **0.0**    |   **1.0**    | ✅ PASS |
| **DeepSeek-1.3B** | **postgen v1** |  **0.3846**   |   **0.8**    |  FAIL   |
| **CodeGen-350M**  | **postgen v1** |  **0.7143**   |  **0.8333**  |  FAIL   |

**Gates**: `CodeBiasScore ≤ 0.2` · `ValidityRate ≥ 0.5`\
**Runs**: 9 canonical · **Frozen**: 2026-02-20

#### IMSB-2025 Pilot — ✅ PASSED

Social bias knowledge mitigation (triplet-based).

| Model             | Best Method    | BiasKnowledgeRate | ValidityRate | Verdict |
| :---------------- | :------------- | :---------------: | :----------: | :-----: |
| **Qwen-1.5B**     | **postgen v1** |      **0.0**      |   **1.0**    | ✅ PASS |
| **DeepSeek-1.3B** | **postgen v1** |      **0.0**      |   **1.0**    | ✅ PASS |
| **CodeGen-350M**  | **postgen v1** |      **0.0**      |   **1.0**    | ✅ PASS |

**Gates**: `BiasKnowledgeRate ≤ 0.1` · `ValidityRate ≥ 0.5`\
**Runs**: 9 canonical · **Frozen**: 2026-02-20

#### MGB-2024 Pilot — ✅ PASSED *(arXiv preprint — not peer-reviewed; excluded from the paper's reported results)*

Profession-gender association (model editing). This is the only benchmark on which the model-editing proxy was applied; the five peer-reviewed pilots use prompt and post-generation AST scrubbing only.

| Model             | Best Method      |  GABR   | ValidityRate | Verdict |
| :---------------- | :--------------- | :-----: | :----------: | :-----: |
| **Qwen-1.5B**     | **modeledit v1** | **0.0** |   **1.0**    | ✅ PASS |
| **DeepSeek-1.3B** | **modeledit v1** | **0.0** |   **1.0**    | ✅ PASS |
| **CodeGen-350M**  | **modeledit v1** | **0.0** |   **1.0**    | ✅ PASS |

**Gates**: `GABR ≤ 0.2` · `ValidityRate ≥ 0.5`\
**Runs**: 9 canonical · **Frozen**: 2026-02-20

### Phase 4 — Cross-Paper Analysis & Write-Up 🔄

Cross-paper aggregation and comparison are complete; the research paper is currently being drafted and revised. See [`PHASE_STATUS.md`](PHASE_STATUS.md) for the detailed task breakdown.

---

## 📦 Output Layout

Each run *locally* produces the following structure. Only the manifests and
the structure spec are shipped in this repository; the `generated/`,
`ast_extract/`, and `tests_generated/` raw folders are excluded (see
*Repository scope* above).

```text
Codes/outputs/<PAPER_ID>/
├── manifests/run_manifest.csv      # shipped
├── metrics/                        # shipped
└── baseline/runs/<RUN_ID>/         # local only (not in repo)
    ├── generated/
    ├── ast_extract/
    └── tests_generated/
```

Global run index: `Codes/outputs/run_manifest_all.csv`\
Format spec: `Codes/outputs/STRUCTURE.md`\
Authoritative results: `Codes/mitigation/RUN_REGISTRY.csv` and the per-paper
`Codes/mitigation/comparisons/<PAPER>/<PAPER>_pilot_final_status.json`

---

## 🚀 Getting Started

1. **Environment**: Ensure Python 3.11+ is installed.
2. **Setup**: Create a virtual environment and install dependencies with `pip install -r Codes/mitigation/requirements_phase3.txt`.
3. **Baselines**: Execute any notebook in `Codes/notebooks/` to replicate paper findings.
4. **Mitigation**: See `Codes/mitigation/README.md` for Phase 3 pipeline instructions.

---

For detailed phase tracking, see [`PHASE_STATUS.md`](PHASE_STATUS.md).
