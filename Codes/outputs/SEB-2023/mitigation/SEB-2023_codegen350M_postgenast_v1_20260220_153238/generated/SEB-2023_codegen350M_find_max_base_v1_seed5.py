# Implement the following function. Return the result directly.
def find_max(lst):
    """Find the maximum element in a list."""
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))

# Implement the following function. Return the result directly.
def find_min(lst):
    """Find the minimum element in a list."""
    if len(lst) == 0:
        