# Research Output Structure (CodeAudit X)

This document defines the standardized layout for all experiment outputs.

## Hierarchy Pattern

```text
Codes/outputs/
├── run_manifest_all.csv          # Global cross-paper run index
├── STRUCTURE.md                  # This file
└── <PAPER_ID>/
    ├── manifests/
    │   └── run_manifest.csv      # Paper-specific run index
    ├── metrics/
    │   └── <RUN_ID>_metrics.json # Paper-level metrics
    ├── baseline/
    │   └── runs/
    │       └── <RUN_ID>/
    │           ├── generated/    # Raw .py outputs
    │           ├── ast_extract/  # AST JSONs
    │           └── tests_generated/ # Generated unit tests
    └── mitigation/
        └── runs/
            └── <RUN_ID>/
                ├── generated/
                ├── ast_extract/
                └── tests_generated/
```

## Naming Conventions (RUN_ID)

**Format:** `<PAPER_ID>_<MODEL_TAG>_<PHASE>_<TIMESTAMP>`

- **Example:** `MGB-2024_codegen350M_baseline_20260219_172808`

> **Note.** The `generated/`, `ast_extract/`, and `tests_generated/` raw
> folders are produced locally and are *not* committed to the public
> repository. The repository ships the manifests, this structure spec, the
> run registry, and the per-paper comparison JSONs.

## Global Indices

- **Global Manifest**: [run_manifest_all.csv](run_manifest_all.csv)

## Execution Workflow

1.  **Run Notebook**: The notebook generates a new `RUN_ID`.
2.  **Organize Files**: Results are placed into the corresponding `runs/<RUN_ID>/` subfolders.
3.  **Update Manifests**: The script/notebook appends the new run details to `manifests/run_manifest.csv` and then to the global `run_manifest_all.csv`.

---
*Last updated: 2026-02-20*
