import json, os, glob
from datetime import datetime
from extract_ast import extract_bu_ast
from bu_metrics import compute_bu_metrics

def normalize_logic(code_string):
    """
    Strips comments and extraneous logic to keep only the core decision block.
    For this pilot, we keep the first function's logic.
    """
    lines = code_string.splitlines()
    cleaned = []
    in_function = False
    for line in lines:
        if line.strip().startswith("def "):
            in_function = True
            cleaned.append(line)
        elif in_function:
            if line.strip().startswith("def ") or (line.strip() and not line.startswith("    ") and not line.startswith("\t")):
                break
            cleaned.append(line)
    return "\n".join(cleaned)

def run_postgen(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
    
    src_run_id = config["source_run_id"]
    model_tag = config["model_tag"]
    src_dir = f"Codes/mitigation/runs/{src_run_id}/generated"
    
    print(f"Starting Post-Gen Normalization: {src_run_id}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"BU-2024_{model_tag}_postgenast_v1_{timestamp}"
    run_dir = f"Codes/mitigation/runs/{run_id}"
    gen_dir = os.path.join(run_dir, "generated")
    ast_dir = os.path.join(run_dir, "ast_extract")
    os.makedirs(gen_dir, exist_ok=True)
    os.makedirs(ast_dir, exist_ok=True)
    
    files = glob.glob(os.path.join(src_dir, "*.py"))
    all_extractions = []
    
    for fpath in files:
        with open(fpath, "r") as f:
            code = f.read()
        
        norm_code = normalize_logic(code)
        
        fname = os.path.basename(fpath)
        with open(os.path.join(gen_dir, fname), "w") as f:
            f.write(norm_code)
            
        ext = extract_bu_ast(norm_code)
        # Parse metadata from filename
        parts = fname.replace(".py", "").split("_")
        # BU-2024_codegen350M_career_choice_base_s1
        ext["task_id"] = "_".join(parts[2:-2])
        ext["variant_id"] = parts[-2]
        ext["seed"] = int(parts[-1][1:])
        
        with open(os.path.join(ast_dir, fname.replace(".py", ".json")), "w") as f:
            json.dump(ext, f, indent=2)
        all_extractions.append(ext)
        
    metrics = compute_bu_metrics(all_extractions, len(files))
    with open(os.path.join(run_dir, f"{run_id}_refined_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
        
    # Mirror
    mirror_dir = f"Codes/outputs/BU-2024/mitigation/{run_id}"
    os.makedirs(mirror_dir, exist_ok=True)
    os.system(f"cp -r {run_dir}/* {mirror_dir}/")
    print(f"Postgen complete. Metrics: {metrics}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python postgen_bu_ast.py <config_path>")
    else:
        run_postgen(sys.argv[1])
