import ast as python_ast

def extract_seb_ast(code_string):
    """
    Extracts SEB-specific structural features from generated code.
    Focuses on the FIRST function definition's return structure.
    """
    result = {
        "parse_ok": False,
        "function_count": 0,
        "first_function_name": None,
        "return_type": "unknown",
        "has_return": False,
        "return_expression_type": None,
        "line_count": 0,
        "errors": None
    }

    try:
        tree = python_ast.parse(code_string)
        result["parse_ok"] = True
    except SyntaxError as e:
        result["errors"] = str(e)
        return result

    result["line_count"] = len(code_string.strip().splitlines())

    functions = [n for n in python_ast.walk(tree) if isinstance(n, python_ast.FunctionDef)]
    result["function_count"] = len(functions)

    if not functions:
        result["return_type"] = "no_function"
        return result

    first_fn = functions[0]
    result["first_function_name"] = first_fn.name

    # Find return statements in the first function
    returns = []
    for node in python_ast.walk(first_fn):
        if isinstance(node, python_ast.Return) and node.value is not None:
            returns.append(node)

    if not returns:
        result["return_type"] = "no_return"
        return result

    result["has_return"] = True
    ret_val = returns[0].value

    # Classify the return expression
    if isinstance(ret_val, python_ast.Compare):
        result["return_type"] = "comparison"
        result["return_expression_type"] = "direct_compare"
    elif isinstance(ret_val, python_ast.BoolOp):
        result["return_type"] = "bool_op"
    elif isinstance(ret_val, python_ast.Constant):
        if isinstance(ret_val.value, bool):
            result["return_type"] = "bool_literal"
        else:
            result["return_type"] = "literal"
    elif isinstance(ret_val, python_ast.Name):
        result["return_type"] = "variable"
    elif isinstance(ret_val, python_ast.Call):
        result["return_type"] = "call"
    elif isinstance(ret_val, python_ast.BinOp):
        result["return_type"] = "binop"
    elif isinstance(ret_val, python_ast.Subscript):
        result["return_type"] = "subscript"
    elif isinstance(ret_val, python_ast.UnaryOp):
        result["return_type"] = "unary"
    elif isinstance(ret_val, python_ast.IfExp):
        result["return_type"] = "ternary"
    elif isinstance(ret_val, python_ast.ListComp) or isinstance(ret_val, python_ast.GeneratorExp):
        result["return_type"] = "comprehension"
    else:
        result["return_type"] = type(ret_val).__name__

    # Check if function body uses if/else (branching approach vs direct return)
    has_if = any(isinstance(n, python_ast.If) for n in python_ast.walk(first_fn))
    if has_if and result["return_type"] in ("bool_literal", "literal", "variable"):
        result["return_type"] = "conditional_branch"

    return result
