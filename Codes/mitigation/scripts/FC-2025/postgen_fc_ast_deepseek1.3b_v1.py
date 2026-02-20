import json
import ast
import astunparse
import re
import csv
import shutil
from pathlib import Path
from datetime import datetime

# --- Configuration ---
CONFIG_PATH = Path("Codes/mitigation/configs/FC-2025/fc_postgen_deepseek1.3b_v1.json")
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

PAPER_ID = config["paper_id"]
SOURCE_RUN_ID = config["source_run_id"]
PROTECTED_ATTRS = set(config["protected_attrs"])
ALLOWED_ATTRS = set(config["allowed_attrs"])

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_ID = f"{PAPER_ID}_deepseek1.3b_postgenast_v1_{TIMESTAMP}"

ROOT = Path.cwd()
SOURCE_DIR = ROOT / "Codes" / "mitigation" / "runs" / SOURCE_RUN_ID / "generated"
RUN_DIR = ROOT / "Codes" / "mitigation" / "runs" / RUN_ID
GEN_DIR = RUN_DIR / "generated"
AST_DIR = RUN_DIR / "ast_extract"
LOG_DIR = RUN_DIR / "logs"
SHADOW_OUTPUT_DIR = ROOT / "Codes" / "outputs" / PAPER_ID / "mitigation" / RUN_ID

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
    audit = {"original_parse_ok": True, "scrubbed_hits": 0, "errors": None}
    if not code_str:
        audit["original_parse_ok"] = False
        return "", audit
    try:
        tree = ast.parse(code_str)
        scrubber = ProtectedAttrScrubber(PROTECTED_ATTRS)
        modified_tree = scrubber.visit(tree)
        ast.fix_missing_locations(modified_tree)
        audit["scrubbed_hits"] = scrubber.hits
        new_code = astunparse.unparse(modified_tree)
        return new_code, audit
    except Exception as e:
        audit["original_parse_ok"] = False
        audit["errors"] = str(e)
        return code_str, audit

def extract_refined_metrics(code_str: str):
    info = {"parse_ok": True, "protected_name_hits": [], "protected_subscript_hits": [], "string_echo_hits": [], "errors": None}
    if not code_str:
        info["parse_ok"] = False
        return info
    try:
        tree = ast.parse(code_str)
        class V(ast.NodeVisitor):
            def visit_Name(self, node):
                if node.id.lower() in PROTECTED_ATTRS: info["protected_name_hits"].append(node.id.lower())
                self.generic_visit(node)
            def visit_Subscript(self, node):
                try:
                    if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                        if node.slice.value.lower() in PROTECTED_ATTRS: info["protected_subscript_hits"].append(node.slice.value.lower())
                except Exception: pass
                self.generic_visit(node)
        V().visit(tree)
    except Exception as e:
        info["parse_ok"] = False
        info["errors"] = str(e)
    ast_hits = set(info["protected_name_hits"] + info["protected_subscript_hits"])
    lowered = code_str.lower()
    for p in PROTECTED_ATTRS:
        if p in lowered and p not in ast_hits: info["string_echo_hits"].append(p)
    return info

# --- Execution ---
print(f"Starting Post-Gen AST Mitigation: {RUN_ID}")
results_index = []
ast_data = []

source_files = list(SOURCE_DIR.glob("*.py"))
if not source_files:
    print(f"ERROR: No source files found for {SOURCE_RUN_ID} at {SOURCE_DIR}")
    exit(1)

print(f"Scrubbing {len(source_files)} files from {SOURCE_RUN_ID}...")
for fpath in source_files:
    original_code = fpath.read_text(encoding="utf-8")
    scrubbed_code_str, audit = scrub_code(original_code)
    
    out_path = GEN_DIR / fpath.name
    out_path.write_text(scrubbed_code_str, encoding="utf-8")
    
    metrics = extract_refined_metrics(scrubbed_code_str)
    entry = {"file": fpath.name, "audit": audit, "metrics": metrics}
    
    ast_path = AST_DIR / f"{fpath.stem}.ast.json"
    ast_path.write_text(json.dumps(entry, indent=2))
    
    ast_data.append(entry)
    results_index.append({"file": fpath.name, "scrubbed": audit["scrubbed_hits"] > 0, "valid": metrics["parse_ok"]})

total = len(ast_data)
valid = sum(1 for r in ast_data if r["metrics"]["parse_ok"])
protected_usage = sum(1 for r in ast_data if r["metrics"]["protected_name_hits"] or r["metrics"]["protected_subscript_hits"])
echo_hits = sum(1 for r in ast_data if r["metrics"]["string_echo_hits"])

summary = {
    "run_id": RUN_ID, "paper_id": PAPER_ID, "method": "postgen_ast_v1", "source_run_id": SOURCE_RUN_ID,
    "ValidityRate": valid / total if total else 0, "CodeLevelProtectedUsageRate": protected_usage / total if total else 0,
    "StringEchoRate": echo_hits / total if total else 0,
    "total": total, "valid": valid, "protected_usage": protected_usage, "timestamp": datetime.now().isoformat()
}

metrics_path = RUN_DIR / f"{RUN_ID}_metrics.json"
metrics_path.write_text(json.dumps(summary, indent=2))
refined_metrics_path = RUN_DIR / f"{RUN_ID}_refined_metrics.json"
refined_metrics_path.write_text(json.dumps(summary, indent=2))

print(f"Mirroring to {SHADOW_OUTPUT_DIR}")
for f in GEN_DIR.glob("*"): shutil.copy(f, SHADOW_OUTPUT_DIR)
shutil.copy(metrics_path, SHADOW_OUTPUT_DIR)
shutil.copy(refined_metrics_path, SHADOW_OUTPUT_DIR)

# Register Run
REGISTRY_PATH = ROOT / "Codes" / "mitigation" / "RUN_REGISTRY.csv"
reg_entry = [RUN_ID, PAPER_ID, "deepseek1.3b", "postgen_ast_v1", "1..5", TIMESTAMP, "completed", str(CONFIG_PATH), str(RUN_DIR), str(refined_metrics_path), f"Post-gen AST scrub from {SOURCE_RUN_ID}"]
with open(REGISTRY_PATH, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(reg_entry)
print("Run complete.")
