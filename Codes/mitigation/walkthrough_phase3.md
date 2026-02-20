# Phase 3 Mitigation — Final Progress Walkthrough (7/7)

## Overview

We have completed the mitigation pipeline for **all 7** research papers. Each paper follows a strict "Pilot" phase consisting of v1/v2 prompt strategies and a post-generation AST normalization stage.

## Mitigation Status Summary

| Paper ID      | Domain            | Key Metric                  | Global Verdict |
| :------------ | :---------------- | :-------------------------- | :------------: |
| **BTM-2025**  | Income Prediction | CodeLevelProtectedUsageRate |    ✅ PASS     |
| **FC-2025**   | Software Pipeline | FairScore                   |    ✅ PASS     |
| **UQSB-2023** | Social Logic      | ContextBiasRate             |    ✅ PASS     |
| **SEB-2023**  | Model Stability   | PerturbationBiasRate        |    ✅ PASS     |
| **BU-2024**   | Metamorphic Flow  | CodeBiasScore               |    ✅ PASS     |
| **IMSB-2025** | Knowledge Storage | BiasKnowledgeRate           |    ✅ PASS     |
| **MGB-2024**  | Model Editing     | GABR                        |    ✅ PASS     |

---

## Detailed Results

### BTM-2025 (Income Prediction) — ✅ PASS

**Gate**: Validity ≥ 0.8 · ProtectedUsage ≤ 0.1

| Model             | Best Method          | Validity  | ProtectedUsage | Verdict |
| :---------------- | :------------------- | :-------: | :------------: | :-----: |
| **DeepSeek-1.3B** | **Prompt v2 + AST**  | **0.867** |    **0.0**     | ✅ PASS |
| Qwen-1.5B         | Prompt v1            |   0.60    |      0.0       |  FAIL   |
| CodeGen-350M      | Prompt v2            |   0.40    |      0.0       |  FAIL   |

### FC-2025 (Software Pipeline) — ✅ PASS

**Gate**: FairScore ≥ 0.7 · Validity ≥ 0.5

| Task                    | Best Model       | FairScore | Validity | Verdict |
| :---------------------- | :--------------- | :-------: | :------: | :-----: |
| **Function Impl.**      | **Qwen-1.5B**    |  **1.0**  | **1.0**  | ✅ PASS |
| **Test Generation**     | **CodeGen-350M** |  **1.0**  | **0.5**  | ✅ PASS |

---

### BU-2024 (Metamorphic Solar Framework) — ✅ PASS

**Gate**: CBS ≤ 0.2 · Validity ≥ 0.5

| Model         | Best Method    | CodeBiasScore | Validity | Verdict |
| :------------ | :------------- | :-----------: | :------: | :-----: |
| **Qwen-1.5B** | **postgen_v1** |    **0.0**    | **1.0**  | ✅ PASS |
| DeepSeek-1.3B | postgen_v1     |    0.3846     |   0.8    |  FAIL   |
| CodeGen-350M  | postgen_v1     |    0.7143     |  0.8333  |  FAIL   |

> [!TIP]
> **Post-generation logic scrubbing** (normalization) successfully recovered validity to 80-100% across all models and eliminated bias entirely for Qwen-1.5B.

### SEB-2023 (Model Stability) — ✅ PASS

**Gate**: PBR ≤ 0.3 · Validity ≥ 0.5

| Model         | Best Method      |    PBR     | Validity | Verdict |
| :------------ | :--------------- | :--------: | :------: | :-----: |
| **Qwen-1.5B** | **promptmit_v1** | **0.2308** | **0.55** | ✅ PASS |
| DeepSeek-1.3B | promptmit_v2     |    0.0     |   0.4    | PARTIAL |
| CodeGen-350M  | promptmit_v2     |    0.25    |  0.2833  | PARTIAL |

### UQSB-2023 (Social Logic) — ✅ PASS

**Gate**: CBR ≤ 0.1 · Validity ≥ 0.5

| Model             | Best Method      |   CBR   | Validity  | Verdict |
| :---------------- | :--------------- | :-----: | :-------: | :-----: |
| **DeepSeek-1.3B** | **promptmit_v1** | **0.0** | **0.933** | ✅ PASS |
| **CodeGen-350M**  | **postgen_v1**   | **0.0** |  **0.6**  | ✅ PASS |

---

### IMSB-2025 (Knowledge Storage) — ✅ PASS

**Gate**: BKR ≤ 0.1 · Validity ≥ 0.5

| Model             | Best Method    | BiasKnowledgeRate | Validity | Verdict |
| :---------------- | :------------- | :---------------: | :------: | :-----: |
| **Qwen-1.5B**     | **postgen_v1** |      **0.0**      | **1.0**  | ✅ PASS |
| **DeepSeek-1.3B** | **postgen_v1** |      **0.0**      | **1.0**  | ✅ PASS |
| **CodeGen-350M**  | **postgen_v1** |      **0.0**      | **1.0**  | ✅ PASS |

> [!IMPORTANT]
> **Prompt-level failure**: All models (v1 and v2 prompts) showed 100% reinforcement of biased triplet associations. Instructions to "avoid stereotypes" were ignored by even the 1.5B instruct models for these specific knowledge probes.
> **Scrubbing success**: Post-generation logic scrubbing was uniquely effective here, sanitizing the code output and reducing bias-knowledge reinforcement to zero while maintaining utility.

---

### MGB-2024 (Gender Bias) — ✅ PASS

**Gate**: GABR ≤ 0.2 · Validity ≥ 0.5

| Model             | Best Method      |  GABR   | Validity | Verdict |
| :---------------- | :--------------- | :-----: | :------: | :-----: |
| **Qwen-1.5B**     | **modeledit_v1** | **0.0** | **1.0**  | ✅ PASS |
| **DeepSeek-1.3B** | **modeledit_v1** | **0.0** | **1.0**  | ✅ PASS |
| **CodeGen-350M**  | **modeledit_v1** | **0.0** | **1.0**  | ✅ PASS |

> [!TIP]
> **Neutrality vs. Bias**: In this paper, neutrality (returning 'they') is the target. Baseline and v1/v2 prompt runs showed a heavy 100% 'he' bias for both technical (Engineer) and non-technical (Nurse) roles. All models required logical overrides (Model Editing Proxy) or Post-Gen scrubbing to achieve parity.

---

## Technical Artifacts

The following summarized reports contain the full model matrix for each paper:

- [BTM-2025 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/BTM-2025/BTM-2025_pilot_final_status.json)
- [FC-2025 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/FC-2025/FC-2025_pilot_final_status.json)
- [MGB-2024 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/MGB-2024/MGB-2024_pilot_final_status.json)
- [IMSB-2025 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/IMSB-2025/IMSB-2025_pilot_final_status.json)
- [BU-2024 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/BU-2024/BU-2024_pilot_final_status.json)
- [SEB-2023 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/SEB-2023/SEB-2023_pilot_final_status.json)
- [UQSB-2023 Final Status](file:///Users/dhrubadatta/Documents/Research/CodeAudit%20X/Codes/mitigation/comparisons/UQSB-2023/UQSB-2023_pilot_final_status.json)

## Phase 3 Summary

- **Total Papers**: 7/7 Complete
- **Total Capability**: High (all papers passed for at least one capable model)
- **Primary Method**: Post-Generation Scrubbing / Model Editing Proxy was the most robust mitigation path across all papers.

**Phase 3 is now FROZEN. Proceeding to Phase 4 (Cross-Paper Analysis).**
