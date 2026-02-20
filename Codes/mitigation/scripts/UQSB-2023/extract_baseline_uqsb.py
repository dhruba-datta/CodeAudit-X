"""
Retroactively extract UQSB-2023 metrics from the Phase 2 baseline codegen350M run.
"""
import json
import os
import glob
from extract_ast import extract_uqsb_ast
from uqsb_metrics import compute_uqsb_metrics

baseline_id = "UQSB-2023_codegen350M_baseline_20260219_175711"
gen_dir = f"Codes/outputs/UQSB-2023/baseline/runs/{baseline_id}/generated"
metrics_dir = "Codes/outputs/UQSB-2023/metrics"
os.makedirs(metrics_dir, exist_ok=True)

gen_files = sorted(glob.glob(os.path.join(gen_dir, "*.py")))
print(f"Found {len(gen_files)} baseline generated files.")

all_extractions = []
for gf in gen_files:
    with open(gf) as f:
        code = f.read()
    
    # Determine attribute from filename
    probe_attr = "ethnicity"  # default for baseline
    for attr in ["ethnicity", "religion", "gender"]:
        if attr in os.path.basename(gf):
            probe_attr = attr
            break
    
    ext = extract_uqsb_ast(code, probe_attr)
    ext["file"] = gf
    
    if ext["parse_ok"]:
        all_extractions.append(ext)
        print(f"  {os.path.basename(gf)}: parse_ok={ext['parse_ok']}, uses_sensitive={ext['uses_sensitive_in_logic']}")
    else:
        print(f"  {os.path.basename(gf)}: PARSE FAILED - {ext['errors']}")

# The baseline only had 1 generation, so total_expected = 1
metrics = compute_uqsb_metrics(all_extractions, total_expected_generations=len(gen_files) if gen_files else 1)

metrics_file = os.path.join(metrics_dir, f"UQSB-2023_codegen350M_baseline_metrics.json")
with open(metrics_file, "w") as f:
    json.dump(metrics, f, indent=2)

print(f"\nExtracted Baseline UQSB-2023 metrics to {metrics_file}:")
print(json.dumps(metrics, indent=2))
