"""
Post-fix script:
1. Patches all FC-2025 refined_metrics.json files where ValidityRate==0.0 
   had FairScore=1.0 -> now FairScore="NA"
2. Identifies canonical (final) runs vs old/duplicate runs
3. Moves old runs to _archive
"""
import json, os, shutil, glob

RUNS_DIR = "Codes/mitigation/runs"
OUTPUTS_DIR = "Codes/outputs/FC-2025/mitigation"
ARCHIVE_DIR = os.path.join(RUNS_DIR, "_archive")
ARCHIVE_OUTPUTS = os.path.join(OUTPUTS_DIR, "_archive")
os.makedirs(ARCHIVE_DIR, exist_ok=True)
os.makedirs(ARCHIVE_OUTPUTS, exist_ok=True)

# ── Step 1: Patch all affected metrics ──────────────────────────────────
patched = 0
for run_name in os.listdir(RUNS_DIR):
    if not run_name.startswith("FC-2025_"):
        continue
    metrics_file = os.path.join(RUNS_DIR, run_name, f"{run_name}_refined_metrics.json")
    if not os.path.exists(metrics_file):
        continue
    with open(metrics_file) as f:
        data = json.load(f)
    
    # Patch: if ValidityRate is 0.0 (or TotalValid is 0) and FairScore is 1.0
    vr = data.get("ValidityRate", None)
    fs = data.get("FairScore", None)
    tv = data.get("TotalValid", None)
    
    needs_patch = False
    if vr == 0.0 and fs == 1.0:
        needs_patch = True
    if tv == 0 and fs == 1.0:
        needs_patch = True
        
    if needs_patch:
        data["RefusalRate"] = "NA"
        data["PreferenceEntropy"] = "NA"
        data["FairScore"] = "NA"
        with open(metrics_file, "w") as f:
            json.dump(data, f, indent=2)
        # Also patch mirrored copy
        mirror = os.path.join(OUTPUTS_DIR, run_name, f"{run_name}_refined_metrics.json")
        if os.path.exists(mirror):
            with open(mirror, "w") as f:
                json.dump(data, f, indent=2)
        patched += 1
        print(f"  PATCHED: {run_name}")

print(f"\nPatched {patched} metrics files.\n")

# ── Step 2: Identify canonical runs vs archive candidates ───────────────
# Canonical runs are the LATEST run per (model, task, method) tuple.
# Pre-refactor runs (without function_implementation/test_case_generation) are always archived.

canonical = {}  # key: (model, task, method) -> run_name (latest by timestamp)

for run_name in sorted(os.listdir(RUNS_DIR)):
    if not run_name.startswith("FC-2025_") or run_name == "_archive":
        continue
    
    parts = run_name.split("_")
    # New format: FC-2025_<model>_<task...>_<method>_<timestamp>
    # Old format: FC-2025_<model>_<method>_<timestamp>
    
    model = parts[1]  # codegen350M, qwen1.5b, deepseek1.3b
    
    # Detect if this is a new-format run (has function_implementation or test_case_generation)
    has_task = "function_implementation" in run_name or "test_case_generation" in run_name
    
    if not has_task:
        # Old pre-refactor run -> archive
        key = None  # will be archived
    else:
        # Extract task and method
        if "function_implementation" in run_name:
            task = "function_implementation"
            remainder = run_name.split("function_implementation_")[1]
        else:
            task = "test_case_generation"
            remainder = run_name.split("test_case_generation_")[1]
        
        # remainder is like: promptmit_v1_20260220_122709
        method_parts = remainder.split("_")
        method = f"{method_parts[0]}_{method_parts[1]}"  # promptmit_v1, postgenast_v1
        
        key = (model, task, method)
    
    if key is None:
        # Pre-refactor -> archive
        print(f"  ARCHIVE (pre-refactor): {run_name}")
        src = os.path.join(RUNS_DIR, run_name)
        dst = os.path.join(ARCHIVE_DIR, run_name)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
        # Also archive mirrored output
        src_out = os.path.join(OUTPUTS_DIR, run_name)
        dst_out = os.path.join(ARCHIVE_OUTPUTS, run_name)
        if os.path.exists(src_out) and not os.path.exists(dst_out):
            shutil.move(src_out, dst_out)
    else:
        # Keep the latest run per key (sorted order = alphabetical = chronological)
        if key in canonical:
            # Archive the older one
            old_run = canonical[key]
            print(f"  ARCHIVE (superseded): {old_run}")
            src = os.path.join(RUNS_DIR, old_run)
            dst = os.path.join(ARCHIVE_DIR, old_run)
            if os.path.exists(src) and not os.path.exists(dst):
                shutil.move(src, dst)
            src_out = os.path.join(OUTPUTS_DIR, old_run)
            dst_out = os.path.join(ARCHIVE_OUTPUTS, old_run)
            if os.path.exists(src_out) and not os.path.exists(dst_out):
                shutil.move(src_out, dst_out)
        canonical[key] = run_name

print(f"\n── Canonical Runs ({len(canonical)}) ──")
for key, run_name in sorted(canonical.items()):
    model, task, method = key
    metrics_file = os.path.join(RUNS_DIR, run_name, f"{run_name}_refined_metrics.json")
    if os.path.exists(metrics_file):
        with open(metrics_file) as f:
            m_data = json.load(f)
        fs = m_data.get("FairScore", "NA")
        vr = m_data.get("ValidityRate", "NA")
        fs_str = f"{fs:.4f}" if isinstance(fs, (int, float)) else fs
        vr_str = f"{vr:.4f}" if isinstance(vr, (int, float)) else vr
    else:
        fs_str = "?"
        vr_str = "?"
    print(f"  {model:>14s} | {task:>25s} | {method:>15s} | FS={fs_str} VR={vr_str} | {run_name}")
