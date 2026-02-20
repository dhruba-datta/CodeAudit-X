# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

def find_min(lst):
    """Find the minimum element in a list."""
    min_val = lst[0]
    for i in range(len(lst)):
