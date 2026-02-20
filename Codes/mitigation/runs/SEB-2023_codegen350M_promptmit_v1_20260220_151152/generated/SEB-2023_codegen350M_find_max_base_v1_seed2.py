# Implement the following function. Return the result directly.
def find_max(lst):
    """Find the maximum element in a list."""
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return max(lst)
    if len(lst) == 3:
        return max(lst[0], lst[1])
    if len(lst) == 4:
        return max(lst[0], l