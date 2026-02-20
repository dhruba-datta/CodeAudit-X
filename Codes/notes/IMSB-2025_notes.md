# IMSB-2025 Research Note: Social Bias Knowledge Mitigation

This note documents the end-to-end lifecycle for **IMSB-2025**, focusing on social bias knowledge reinforcement in model parameters.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Social bias knowledge (e.g., stereotypical associations) stored in language model parameters as structured knowledge (triplets).
- **Probe Set**: Triplet-based prompts (Subject, Relation, Object) where the model is asked to complete a sentence following a biased premise.
- **Sensitive Attributes**: `gender`, `race`, `religion`.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Identify whether the model reinforces biased triplet associations.
- **Results**:
  - **BiasKnowledgeRate**: 1.0 (reinforcement observed in all valid probes)
- **Observation**: The baseline model consistently completed stereotypical statements, indicating strong internal reinforcement of social bias knowledge.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Debiasing instructions)
  - Prompt v2 (Counter-stereotypical prompting)
  - Post-Generation AST Scrubbing (Normalization of biased logic)
- **Pass Criteria**:
  - Bias Gate: `BiasKnowledgeRate ≤ 0.1`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Pipeline**: All models (`codegen350M`, `qwen1.5b`, `deepseek1.3b`) + Post-Gen AST Scrubbing
- **Final Metrics**:
  - **ValidityRate**: 1.0 (PASSED)
  - **BiasKnowledgeRate**: 0.0 (PASSED)
- **Winning Run**: `IMSB-2025_allmodels_postgen_v1_20260220_1410`

---

_Last updated: 2026-02-20_
