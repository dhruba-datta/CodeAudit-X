import json, os, glob
from extract_ast import extract_bu_ast
from bu_metrics import compute_bu_metrics

def extract_baseline():
    baseline_id = "BU-2024_codegen350M_baseline_20260219_175651"
    gen_dir = f"Codes/outputs/BU-2024/baseline/runs/{baseline_id}/generated"
    metrics_dir = "Codes/outputs/BU-2024/metrics"
    os.makedirs(metrics_dir, exist_ok=True)

    gen_files = sorted(glob.glob(os.path.join(gen_dir, "*.py")))
    print(f"Found {len(gen_files)} baseline generated files.")

    all_extractions = []
    for gf in gen_files:
        with open(gf) as f:
            code = f.read()
        ext = extract_bu_ast(code)
        
        # BU-2024_codegen350M_solar_task_01_20260219_175653.py
        # Note: baseline only had 1 task and presumably 1 seed
        ext["task_id"] = "solar_task_01"
        ext["seed"] = 1
        ext["variant_id"] = "base" 
        all_extractions.append(ext)

    # Note: baseline CBS will be NA because there aren't multiple variants in the baseline folder
    # unless we ran them. But the manifest said "Loaded 1 metamorphic tasks" and generated 1 file.
    metrics = compute_bu_metrics(all_extractions, len(gen_files))
    mf = os.path.join(metrics_dir, "BU-2024_codegen350M_baseline_metrics.json")
    with open(mf, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Baseline metrics saved to {mf}")

if __name__ == "__main__":
    extract_baseline()
