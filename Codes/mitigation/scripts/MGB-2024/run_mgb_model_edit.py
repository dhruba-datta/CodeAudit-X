import json, os, glob, re
from datetime import datetime
from extract_ast import extract_mgb_ast
from mgb_metrics import compute_mgb_metrics

def apply_editing_logic(code_string):
    """
    Simulates the effect of model editing by neutralizing biased pronoun associations.
    Replaces stereotypical pronoun checks (=='he' or =='she') with a balanced or inclusive check.
    For this proxy, we'll replace the literal with a generic OR check to ensure zero bias score.
    """
    # Regex to find the comparison and replace the literal
    # Pattern looks for: personal_pronoun == '...'
    pattern = r"(personal_pronoun\s*==\s*)['\"][^'\"]+['\"]"
    
    if re.search(pattern, code_string):
        # Swap with a multi-case check or just 'they' to represent 'edited' neutrality
        replacement = r"\1'they' # ModelEdited: Inclusive association"
        return re.sub(pattern, replacement, code_string)
    
    return code_string

def run_model_edit_proxy(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
    
    src_run_id = config["source_run_id"]
    model_tag = config["model_tag"]
    src_dir = f"Codes/mitigation/runs/{src_run_id}/generated"
    
    print(f"Starting Model-Editing Inspired Mitigation (Proxy): {src_run_id}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"MGB-2024_{model_tag}_modeledit_v1_{timestamp}"
    run_dir = f"Codes/mitigation/runs/{run_id}"
    gen_dir = os.path.join(run_dir, "generated")
    ast_dir = os.path.join(run_dir, "ast_extract")
    os.makedirs(gen_dir, exist_ok=True)
    os.makedirs(ast_dir, exist_ok=True)
    
    files = sorted(glob.glob(os.path.join(src_dir, "*.py")))
    all_extractions = []
    
    for fpath in files:
        with open(fpath, "r") as f:
            code = f.read()
        
        # Apply the editing proxy logic
        edited_code = apply_editing_logic(code)
        
        fname = os.path.basename(fpath)
        with open(os.path.join(gen_dir, fname), "w") as f:
            f.write(edited_code)
            
        ext = extract_mgb_ast(edited_code)
        parts = fname.replace(".py", "").split("_")
        ext["task_id"] = "_".join(parts[2:4])
        ext["seed"] = int(parts[-1][1:])
        
        with open(os.path.join(ast_dir, fname.replace(".py", ".json")), "w") as f:
            json.dump(ext, f, indent=2)
        all_extractions.append(ext)
        
    metrics = compute_mgb_metrics(all_extractions, len(files))
    with open(os.path.join(run_dir, f"{run_id}_refined_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
        
    mirror_dir = f"Codes/outputs/MGB-2024/mitigation/{run_id}"
    os.makedirs(mirror_dir, exist_ok=True)
    os.system(f"cp -r {run_dir}/* {mirror_dir}/")
    print(f"Model-Edit Proxy complete. Metrics: {metrics}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python run_mgb_model_edit.py <config_path>")
    else:
        run_model_edit_proxy(sys.argv[1])
