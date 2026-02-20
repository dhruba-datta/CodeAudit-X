import json
import os
import glob
from fc_metrics import compute_fc_metrics

# The original baseline ID for FC-2025
baseline_id = "FC-2025_codegen350M_baseline_20260219_175654"
ast_dir = f"Codes/outputs/FC-2025/baseline/runs/{baseline_id}/ast_extract"
metrics_dir = f"Codes/outputs/FC-2025/metrics"

os.makedirs(metrics_dir, exist_ok=True)

all_extractions = []
expected_total = 0

# Count the generated python files as expected total
gen_dir = f"Codes/outputs/FC-2025/baseline/runs/{baseline_id}/generated"
if os.path.exists(gen_dir):
    expected_total = len(glob.glob(os.path.join(gen_dir, "*.py")))
    
ast_files = glob.glob(os.path.join(ast_dir, "*.ast.json"))
for af in ast_files:
    with open(af, "r") as f:
        data = json.load(f)
        if "ast_sensitive_usage" in data:
            ast_data = data["ast_sensitive_usage"]
            # To interface with compute_fc_metrics, we just need the dictionary to
            # have any of the protected keys if they were found.
            ext_dict = {}
            # Check the sensitive_string_hits array
            hits = ast_data.get("sensitive_string_hits", [])
            for hit in hits:
                if hit in ["gender", "race", "age"]:
                    ext_dict[hit] = "found" # value doesn't matter for the counter, just presence
            all_extractions.append(ext_dict)

metrics = compute_fc_metrics(all_extractions, total_expected_generations=expected_total)

# In the baseline, we also want to simulate the expected output format
# Codes/outputs/FC-2025/metrics/FC-2025_codegen350M_job_hiring_metrics.json
out_path = os.path.join(metrics_dir, "FC-2025_codegen350M_job_hiring_metrics.json")
with open(out_path, "w") as f:
    json.dump(metrics, f, indent=2)

print(f"Extracted Baseline FC-2025 metrics to {out_path}:")
print(json.dumps(metrics, indent=2))
