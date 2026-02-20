import json, os, glob
from mgb_metrics import compute_mgb_metrics

CANONICAL_RUNS = [
    "MGB-2024_codegen350M_promptmit_v1_20260220_184330",
    "MGB-2024_qwen1.5b_promptmit_v1_20260220_184354",
    "MGB-2024_deepseek1.3b_promptmit_v1_20260220_184430",
    "MGB-2024_codegen350M_promptmit_v2_20260220_184459",
    "MGB-2024_qwen1.5b_promptmit_v2_20260220_184523",
    "MGB-2024_deepseek1.3b_promptmit_v2_20260220_184600",
    "MGB-2024_codegen350M_modeledit_v1_20260220_184644",
    "MGB-2024_qwen1.5b_modeledit_v1_20260220_184644",
    "MGB-2024_deepseek1.3b_modeledit_v1_20260220_184644",
    "MGB-2024_codegen350M_postgenast_v1_20260220_185148",
    "MGB-2024_qwen1.5b_postgenast_v1_20260220_184702",
    "MGB-2024_deepseek1.3b_postgenast_v1_20260220_185148"
]

def update():
    runs_dir = "Codes/mitigation/runs"
    for rid in CANONICAL_RUNS:
        ast_dir = os.path.join(runs_dir, rid, "ast_extract")
        if not os.path.exists(ast_dir):
            print(f"Skipping {rid}, no AST dir")
            continue
            
        ast_files = glob.glob(os.path.join(ast_dir, "*.json"))
        extractions = []
        for af in ast_files:
            with open(af, "r") as f:
                extractions.append(json.load(f))
        
        # total_expected is 15 for these pilots
        metrics = compute_mgb_metrics(extractions, 15)
        
        metrics_file = os.path.join(runs_dir, rid, f"{rid}_refined_metrics.json")
        with open(metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)
            
        # Mirror to outputs
        mirror_dir = f"Codes/outputs/MGB-2024/mitigation/{rid}"
        if os.path.exists(mirror_dir):
            with open(os.path.join(mirror_dir, f"{rid}_refined_metrics.json"), "w") as f:
                json.dump(metrics, f, indent=2)
                
        print(f"Updated {rid}: {metrics}")

if __name__ == "__main__":
    update()
