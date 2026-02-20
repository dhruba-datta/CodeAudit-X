import ast
import json
import argparse
from pathlib import Path

class SensitiveVisitor(ast.NodeVisitor):
    def __init__(self, target_names, target_strings):
        self.target_names = target_names
        self.target_strings = target_strings
        self.found_names = []
        self.found_strings = []
        self.uses_record_indexing = []

    def visit_Name(self, node):
        node_id = node.id.lower()
        if node_id in self.target_names:
            self.found_names.append(node_id)
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            val = node.value.lower()
            if val in self.target_strings:
                self.found_strings.append(val)
        self.generic_visit(node)
        
    def visit_Subscript(self, node):
        # E.g., candidate['gender']
        if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
            val = node.slice.value.lower()
            if val in self.target_strings:
                self.uses_record_indexing.append(val)
        self.generic_visit(node)

def extract_ast(input_path, output_path, sensitive_names, sensitive_strings):
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()

    result_dict = {
        "ast_sensitive_usage": {
            "parse_ok": True,
            "sensitive_name_hits": [],
            "sensitive_string_hits": [],
            "uses_record_indexing": [],
            "errors": None
        }
    }

    try:
        tree = ast.parse(code)
        visitor = SensitiveVisitor(set(sensitive_names), set(sensitive_strings))
        visitor.visit(tree)
        
        # Unique hits
        result_dict["ast_sensitive_usage"]["sensitive_name_hits"] = list(set(visitor.found_names))
        # Keep track of everything matching target string (even outside subscripts, as the paper restricts any generated string reference)
        result_dict["ast_sensitive_usage"]["sensitive_string_hits"] = list(set(visitor.found_strings + visitor.uses_record_indexing + visitor.found_names))
        result_dict["ast_sensitive_usage"]["uses_record_indexing"] = list(set(visitor.uses_record_indexing))
        
    except Exception as e:
        result_dict["ast_sensitive_usage"]["parse_ok"] = False
        result_dict["ast_sensitive_usage"]["errors"] = str(e)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result_dict, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_py", type=str)
    parser.add_argument("output_json", type=str)
    parser.add_argument("--sensitive-names", type=str, default="")
    parser.add_argument("--sensitive-strings", type=str, default="")
    args = parser.parse_args()
    
    names = [n.strip().lower() for n in args.sensitive_names.split(",") if n.strip()]
    strings = [s.strip().lower() for s in args.sensitive_strings.split(",") if s.strip()]
    
    extract_ast(args.input_py, args.output_json, names, strings)
