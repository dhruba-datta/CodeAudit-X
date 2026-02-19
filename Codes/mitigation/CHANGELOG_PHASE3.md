# Phase 3 - Mitigation Changelog

All notable changes to the Phase 3 Mitigation research will be documented in this file.

## [2026-02-19] - Phase 3 Initialization

- Locked Phase 2 state.
- Created directory structure for Phase 3.
- Initialized `RUN_REGISTRY.csv` and `CHANGELOG_PHASE3.md`.

## [2026-02-19] - Phase 3.1: Post-Generation Mitigation (BTM-2025)

- Implemented AST-based identifier/subscript scrubbing in `postgen_btm_ast_v1.py`.
- Source Run: `BTM-2025_codegen350M_promptmit_v2_20260219_190744`.
- **Key Findings**:
  - **CodeLevelProtectedUsageRate: 0.0** (PASSED bias gate).
  - **ValidityRate: 0.4** (FAILED utility gate).
  - Post-gen scrubbing failed to recover validity because source files were mostly empty or syntactically broken.
- Created comparison report: `Codes/mitigation/comparisons/BTM-2025/BTM-2025_codegen350M_postgen_v1_vs_baseline_v2.json`.
- **Final Recommendation**: Prompt-level and post-gen strategies on `codegen-350M-mono` are blocked by the model's low instruction-following capability. **Pivot to a more capable model (e.g., 3B+ parameters)** for the next pilot.
