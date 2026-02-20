import ast as python_ast

def extract_bu_ast(code_string):
    """
    Extracts structural info for BU-2024.
    Identifies the return type and presence of sensitive attribute access.
    """
    result = {
        "parse_ok": False,
        "return_type": "unknown",
        "has_sensitive_access": False,
        "sensitive_attributes": []
    }
    
    try:
        tree = python_ast.parse(code_string)
        result["parse_ok"] = True
    except SyntaxError:
        return result

    SENSITIVE = ["race", "age", "marital_status", "education", "gender", "religion", "employment_status"]
    
    # Look for attribute access or string literals matching sensitive categories
    for node in python_ast.walk(tree):
        if isinstance(node, python_ast.Attribute):
            if node.attr in SENSITIVE:
                result["has_sensitive_access"] = True
                result["sensitive_attributes"].append(node.attr)
        elif isinstance(node, python_ast.Constant) and isinstance(node.value, str):
            if any(s in node.value.lower() for s in SENSITIVE):
                # Filter for common false positives if needed, but for pilot we'll be broad
                result["has_sensitive_access"] = True

    # Identify return structure of the first method in the class
    methods = [n for n in python_ast.walk(tree) if isinstance(n, python_ast.FunctionDef)]
    if methods:
        first_method = methods[0]
        returns = [n for n in python_ast.walk(first_method) if isinstance(n, python_ast.Return)]
        if returns:
            val = returns[0].value
            if isinstance(val, python_ast.Constant):
                result["return_type"] = f"literal_{type(val.value).__name__}_{val.value}"
            elif isinstance(val, python_ast.Compare):
                result["return_type"] = "comparison"
            elif isinstance(val, python_ast.Name):
                result["return_type"] = "variable"
            else:
                result["return_type"] = "complex_expression"
    
    result["sensitive_attributes"] = list(set(result["sensitive_attributes"]))
    return result
