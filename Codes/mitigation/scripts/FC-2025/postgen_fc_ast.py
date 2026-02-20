import os
import sys
import json
import ast
import astunparse
import csv
import shutil
import datetime
from pathlib import Path

from fc_metrics import compute_fc_metrics

def scrub():
    if len(sys.argv) < 2:
        print("Usage: python postgen_fc_ast.py <path_to_config>")
        sys.exit(1)
        
    config_path = sys.argv[1]
    with open(config_path, "r") as f:
        config = json.load(f)
        
    PAPER_ID = config["paper_id"]
    SOURCE_RUN_ID = config["source_run_id"]
    PROTECTED_ATTRS = set(config["protected_attrs"])
    ALLOWED_ATTRS = set(config["allowed_attrs"])
    
    # Infer task type and model tag from the source run ID (e.g. FC-2025_codegen350M_function_implementation_promptmit_v1_TIMESTAMP)
    # Actually wait, the run_ids generated are like: FC-2025_codegen350M_function_implementation_promptmit_v1_20260220_123000
    parts = SOURCE_RUN_ID.split("_")
    model_tag = parts[1]
    
    # Task type might be multiple words
    # FC-2025_tag_function_implementation_...
    # Let's just find where promptmit is
    try:
        p_idx = parts.index("promptmit")
        task_type = "_".join(parts[2:p_idx])
    except:
        task_type = "unknown_task"

    TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    RUN_ID = f"{PAPER_ID}_{model_tag}_{task_type}_postgenast_v1_{TIMESTAMP}"
    
    ROOT = Path.cwd()
    SOURCE_DIR = ROOT / "Codes" / "mitigation" / "runs" / SOURCE_RUN_ID / "generated"
    RUN_DIR = ROOT / "Codes" / "mitigation" / "runs" / RUN_ID
    GEN_DIR = RUN_DIR / "generated"
    AST_DIR = RUN_DIR / "ast_extract"
    LOG_DIR = RUN_DIR / "logs"
    SHADOW_OUTPUT_DIR = ROOT / "Codes" / "outputs" / PAPER_ID / "mitigation" / RUN_ID

    if not SOURCE_DIR.exists():
         print(f"ERROR: Source run directory does not exist: {SOURCE_DIR}")
         sys.exit(1)

    for d in [GEN_DIR, AST_DIR, LOG_DIR, SHADOW_OUTPUT_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    class ProtectedAttrScrubber(ast.NodeTransformer):
        def __init__(self, protected_attrs):
            self.protected_attrs = protected_attrs
            self.hits = 0

        def visit_Subscript(self, node):
            try:
                if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                    if node.slice.value.lower() in self.protected_attrs:
                        self.hits += 1
                        return ast.Constant(value="SCRUBBED_ATTR", kind=None)
            except Exception: pass
            return self.generic_visit(node)

        def visit_Name(self, node):
            if node.id.lower() in self.protected_attrs:
                self.hits += 1
                return ast.Name(id="SCRUBBED_ID", ctx=node.ctx)
            return self.generic_visit(node)

    def scrub_code(code_str: str):
        if not code_str:
            return "", False
        try:
            tree = ast.parse(code_str)
            scrubber = ProtectedAttrScrubber(PROTECTED_ATTRS)
            modified_tree = scrubber.visit(tree)
            ast.fix_missing_locations(modified_tree)
            new_code = astunparse.unparse(modified_tree)
            return new_code, True
        except Exception as e:
            return code_str, False

    def extract_fc_metrics(code_str: str):
        info = {"parse_ok": True, "string_hits": []}
        if not code_str:
            info["parse_ok"] = False
            return info
        try:
           ast.parse(code_str)
        except:
           info["parse_ok"] = False
           return info
           
        lowered = code_str.lower()
        for p in PROTECTED_ATTRS:
            if p in lowered:
                info["string_hits"].append(p)
        return info

    print(f"Starting Post-Gen AST Mitigation: {RUN_ID}")
    
    source_files = list(SOURCE_DIR.glob("*.py"))
    print(f"Scrubbing {len(source_files)} files from {SOURCE_RUN_ID}...")
    
    all_extractions = []
    
    for fpath in source_files:
        original_code = fpath.read_text(encoding="utf-8")
        scrubbed_code_str, parse_ok = scrub_code(original_code)
        
        out_path = GEN_DIR / fpath.name
        out_path.write_text(scrubbed_code_str, encoding="utf-8")
        
        metrics = extract_fc_metrics(scrubbed_code_str)
        
        ext_dict = {}
        if parse_ok and metrics["parse_ok"]:
             for hit in metrics["string_hits"]:
                 ext_dict[hit] = "found"
             all_extractions.append(ext_dict)

        entry = {"file": fpath.name, "metrics": metrics}
        ast_path = AST_DIR / f"{fpath.stem}.ast.json"
        ast_path.write_text(json.dumps(entry, indent=2))
        
    fc_metrics = compute_fc_metrics(all_extractions, total_expected_generations=len(source_files))
    
    metrics_path = RUN_DIR / f"{RUN_ID}_refined_metrics.json"
    metrics_path.write_text(json.dumps(fc_metrics, indent=2))

    print(f"Mirroring to {SHADOW_OUTPUT_DIR}")
    for f in GEN_DIR.glob("*"): shutil.copy(f, SHADOW_OUTPUT_DIR)
    shutil.copy(metrics_path, SHADOW_OUTPUT_DIR)

    # Register Run
    REGISTRY_PATH = ROOT / "Codes" / "mitigation" / "RUN_REGISTRY.csv"
    reg_entry = [
        RUN_ID, PAPER_ID, model_tag, f"{task_type}_postgenast_v1", "1..5", TIMESTAMP, "completed", 
        str(config_path), str(RUN_DIR), str(metrics_path), f"Post-gen AST scrub from {SOURCE_RUN_ID}"
    ]
    with open(REGISTRY_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(reg_entry)
        
    print(f"Postgen Run complete. FairScore: {fc_metrics['FairScore']:.4f}")

if __name__ == "__main__":
    scrub()
