# 📋 CodeAudit X — Phase Status

> Last updated: 2026-02-20

---

## Phase 1 — Literature Review & Probe Design ✅

| Task                                              |   Status    |
| :------------------------------------------------ | :---------: |
| Survey 22+ papers on LLM code-generation bias     | ✅ Complete |
| Define bias probe templates per domain            | ✅ Complete |
| Design structured JSON prompts (`Codes/prompts/`) | ✅ Complete |
| Set up Python 3.11 orchestration environment      | ✅ Complete |

**Output**: `Papers/` (22 reference PDFs), `Codes/prompts/` (structured probes)

---

## Phase 2 — Baseline Replications ✅

Replicated all 7 papers to establish baseline bias measurements.

| Paper         | Domain            | Model        | Methodology                   | Status |
| :------------ | :---------------- | :----------- | :---------------------------- | :----: |
| **BTM-2025**  | Income Prediction | CodeGen-350M | Sensitive token usage via AST |   ✅   |
| **FC-2025**   | Software Pipeline | CodeGen-350M | Few-shot scoring fairness     |   ✅   |
| **IMSB-2025** | Knowledge Storage | CodeGen-350M | Triplet-based bias probes     |   ✅   |
| **MGB-2024**  | Model Editing     | CodeGen-350M | Profession-gender association |   ✅   |
| **BU-2024**   | Metamorphic Flow  | CodeGen-350M | Solar framework testing       |   ✅   |
| **UQSB-2023** | Social Logic      | CodeGen-350M | Contextual attribute encoding |   ✅   |
| **SEB-2023**  | Model Stability   | CodeGen-350M | Prompt perturbation analysis  |   ✅   |

**Locked**: 2026-02-19 (Tag: `phase2-complete`)\
**Output**: `Codes/notebooks/`, `Codes/outputs/`, `Codes/notes/`

---

## Phase 3 — Mitigation 🔄

Prompt-level and post-generation mitigation to reduce bias while maintaining code validity.

### BTM-2025 (Income Prediction) — ✅ PASSED

**Pipeline**: `deepseek-coder-1.3b-instruct` + v2 prompt refinement + post-gen AST scrub

| Metric                      |     Value     | Gate  | Status |
| :-------------------------- | :-----------: | :---: | :----: |
| ValidityRate                | 0.867 (13/15) | ≥ 0.8 |   ✅   |
| CodeLevelProtectedUsageRate |      0.0      | ≤ 0.1 |   ✅   |
| StringEchoRate              |     0.133     |  N/A  |   OK   |

**Models evaluated**: CodeGen-350M → Qwen-1.5B → **DeepSeek-1.3B** (winner)\
**Runs**: 12 registered\
**Frozen**: 2026-02-19

### FC-2025 (Software Pipeline) — ✅ PASSED

**Pipeline**: Task-based evaluation with FC-specific metrics (RefusalRate, PreferenceEntropy, FairScore)\
**Tasks**: `function_implementation`, `test_case_generation`\
**Methods**: `promptmit_v1`, `promptmit_v2`, `postgenast_v1`

| Task                    | Best Model       | FairScore | ValidityRate | Gate |
| :---------------------- | :--------------- | :-------: | :----------: | :--: |
| Function Implementation | **Qwen-1.5B**    |  **1.0**  |   **1.0**    |  ✅  |
| Test Case Generation    | **CodeGen-350M** |  **1.0**  |   **0.5**    |  ✅  |

**Models evaluated**: CodeGen-350M, Qwen-1.5B, DeepSeek-1.3B\
**Gates**: `FairScore ≥ 0.7` · `ValidityRate ≥ 0.5`\
**Runs**: 18 canonical\
**Frozen**: 2026-02-20

> **Note**: DeepSeek-1.3B FAILED on FC-2025 (best FairScore=0.667, ValidityRate=0.3). Runs with zero valid outputs return FairScore=NA.

### UQSB-2023 (Social Logic) — ⏳ Pending

Scale winning pipeline. Next active paper.

### Remaining Papers — 📋 Planned

| Paper     | Domain            | Status  |
| :-------- | :---------------- | :-----: |
| IMSB-2025 | Knowledge Storage | Planned |
| MGB-2024  | Model Editing     | Planned |
| BU-2024   | Metamorphic Flow  | Planned |
| SEB-2023  | Model Stability   | Planned |

---

## Phase 4 — Cross-Paper Analysis & Write-Up 📋

| Task                                            | Status  |
| :---------------------------------------------- | :-----: |
| Aggregate mitigation results across all papers  | Planned |
| Statistical comparison (pre vs post mitigation) | Planned |
| Final research report / paper draft             | Planned |

---

## 📂 Key References

| Resource                 | Path                                                                                                                                               |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mitigation pipeline docs | [`Codes/mitigation/README.md`](Codes/mitigation/README.md)                                                                                         |
| Experiment changelog     | [`Codes/mitigation/CHANGELOG_PHASE3.md`](Codes/mitigation/CHANGELOG_PHASE3.md)                                                                     |
| Run registry             | [`Codes/mitigation/RUN_REGISTRY.csv`](Codes/mitigation/RUN_REGISTRY.csv)                                                                           |
| BTM-2025 final status    | [`Codes/mitigation/comparisons/BTM-2025/BTM-2025_pilot_final_status.json`](Codes/mitigation/comparisons/BTM-2025/BTM-2025_pilot_final_status.json) |
| FC-2025 final status     | [`Codes/mitigation/comparisons/FC-2025/FC-2025_pilot_final_status.json`](Codes/mitigation/comparisons/FC-2025/FC-2025_pilot_final_status.json)     |
| Output structure spec    | [`Codes/outputs/STRUCTURE.md`](Codes/outputs/STRUCTURE.md)                                                                                         |
