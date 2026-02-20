# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    if len(lst) == 0:
        return None
    else:
        return lst[0]

def find_min(lst):
    """Find the minimum element in a list."""
    if len(lst) == 0:
        return None
    else:
        return lst[0]

def merge(lst1, lst2):
    """Merge two sorted lists into a new list