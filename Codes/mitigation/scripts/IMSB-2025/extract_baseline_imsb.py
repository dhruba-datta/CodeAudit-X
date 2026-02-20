import json, os, glob
from extract_ast import extract_imsb_ast
from imsb_metrics import compute_imsb_metrics

def extract_baseline():
    baseline_id = "IMSB-2025_codegen350M_baseline_20260219_175659"
    gen_dir = f"Codes/outputs/IMSB-2025/baseline/runs/{baseline_id}/generated"
    metrics_dir = "Codes/outputs/IMSB-2025/metrics"
    os.makedirs(metrics_dir, exist_ok=True)

    task_targets = {
        "triplet_01": "take care of the child",
        "triplet_02": "skilled in mathematics"
    }

    gen_files = sorted(glob.glob(os.path.join(gen_dir, "*.txt")))
    print(f"Found {len(gen_files)} baseline generated files.")

    all_extractions = []
    for gf in gen_files:
        with open(gf) as f:
            code = f.read()
        
        # Determine target object from filename
        bn = os.path.basename(gf)
        tid = "unknown"
        for t in task_targets:
            if t in bn:
                tid = t
                break
        
        ext = extract_imsb_ast(code, task_targets.get(tid))
        ext["task_id"] = tid
        ext["seed"] = 1
        all_extractions.append(ext)

    metrics = compute_imsb_metrics(all_extractions, len(gen_files))
    mf = os.path.join(metrics_dir, "IMSB-2025_codegen350M_baseline_metrics.json")
    with open(mf, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Baseline metrics (IMSB) saved to {mf}")

if __name__ == "__main__":
    extract_baseline()
