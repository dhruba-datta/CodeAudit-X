import json, os, glob
from extract_ast import extract_mgb_ast
from mgb_metrics import compute_mgb_metrics

def extract_baseline():
    baseline_id = "MGB-2024_codegen350M_baseline_20260219_175703"
    gen_dir = f"Codes/outputs/MGB-2024/baseline/runs/{baseline_id}/generated"
    metrics_dir = "Codes/outputs/MGB-2024/metrics"
    os.makedirs(metrics_dir, exist_ok=True)

    gen_files = sorted(glob.glob(os.path.join(gen_dir, "*.py")))
    print(f"Found {len(gen_files)} baseline generated files.")

    all_extractions = []
    for gf in gen_files:
        with open(gf) as f:
            code = f.read()
        
        ext = extract_mgb_ast(code)
        # Extract metadata from filename: MGB-2024_codegen350M_best_nurse_20260219_175705.py
        bn = os.path.basename(gf)
        parts = bn.replace(".py", "").split("_")
        ext["task_id"] = f"{parts[2]}_{parts[3]}"
        ext["seed"] = 1 # baseline seeds are 1 per task
        all_extractions.append(ext)

    metrics = compute_mgb_metrics(all_extractions, len(gen_files))
    mf = os.path.join(metrics_dir, "MGB-2024_codegen350M_baseline_metrics.json")
    with open(mf, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Baseline metrics (MGB) saved to {mf}")

if __name__ == "__main__":
    extract_baseline()
