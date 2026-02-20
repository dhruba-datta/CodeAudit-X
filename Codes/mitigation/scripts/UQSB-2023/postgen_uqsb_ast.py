"""
Post-generation AST scrub for UQSB-2023.
Strips sensitive attribute references from generated code and re-evaluates metrics.
"""
import json
import os
import re
import shutil
import datetime
from pathlib import Path
from extract_ast import extract_uqsb_ast
from uqsb_metrics import compute_uqsb_metrics

NEUTRAL_REPLACEMENTS = {
    "ethnicity": "category",
    "religion": "category",
    "gender": "category",
    "race": "category",
    "age": "value",
    "nationality": "category"
}

def scrub_code(code_string, protected_attrs):
    """Rename sensitive attribute references to neutral terms."""
    scrubbed = code_string
    for attr in protected_attrs:
        neutral = NEUTRAL_REPLACEMENTS.get(attr, "field")
        # Replace variable names and parameter names
        scrubbed = re.sub(r'\b' + attr + r'\b', neutral, scrubbed, flags=re.IGNORECASE)
    return scrubbed

def run_postgen(config_path):
    with open(config_path) as f:
        config = json.load(f)
    
    source_run_id = config["source_run_id"]
    model_tag = config["model_tag"]
    protected_attrs = config["protected_attrs"]
    
    source_dir = Path(f"Codes/mitigation/runs/{source_run_id}")
    gen_dir = source_dir / "generated"
    
    if not gen_dir.exists():
        print(f"ERROR: Source generation dir not found: {gen_dir}")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"UQSB-2023_{model_tag}_postgenast_v1_{timestamp}"
    run_dir = Path(f"Codes/mitigation/runs/{run_id}")
    scrub_gen_dir = run_dir / "generated"
    ast_dir = run_dir / "ast_extract"
    scrub_gen_dir.mkdir(parents=True, exist_ok=True)
    ast_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Starting Post-Gen AST Mitigation: {run_id}")
    
    source_files = sorted(gen_dir.glob("*.py"))
    print(f"Scrubbing {len(source_files)} files from {source_run_id}...")
    
    all_extractions = []
    total = len(source_files)
    
    for src_file in source_files:
        with open(src_file) as f:
            original = f.read()
        
        scrubbed = scrub_code(original, protected_attrs)
        
        out_file = scrub_gen_dir / src_file.name
        with open(out_file, "w") as f:
            f.write(scrubbed)
        
        # Determine probe attribute from filename
        probe_attr = "ethnicity"  # default
        for attr in protected_attrs:
            if attr in src_file.name:
                probe_attr = attr
                break
        
        ext = extract_uqsb_ast(scrubbed, probe_attr)
        ext["source_file"] = str(src_file)
        ext["scrubbed_file"] = str(out_file)
        
        ast_file = ast_dir / (src_file.stem + ".ast.json")
        with open(ast_file, "w") as f:
            json.dump(ext, f, indent=2)
        
        if ext["parse_ok"]:
            all_extractions.append(ext)
    
    metrics = compute_uqsb_metrics(all_extractions, total)
    metrics_file = run_dir / f"{run_id}_refined_metrics.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=2)
    
    # Mirror
    mirror_dir = Path(f"Codes/outputs/UQSB-2023/mitigation/{run_id}")
    if mirror_dir.exists():
        shutil.rmtree(mirror_dir)
    shutil.copytree(run_dir, mirror_dir)
    print(f"Mirroring to {mirror_dir}")
    
    cbr = metrics.get("ContextBiasRate", "NA")
    cbr_str = f"{cbr:.4f}" if isinstance(cbr, (int, float)) else cbr
    print(f"Postgen Run complete. ContextBiasRate: {cbr_str}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python postgen_uqsb_ast.py <config_path>")
        sys.exit(1)
    run_postgen(sys.argv[1])
