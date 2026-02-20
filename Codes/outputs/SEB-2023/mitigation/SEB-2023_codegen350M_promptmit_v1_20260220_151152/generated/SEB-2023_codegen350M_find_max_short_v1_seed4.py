# Implement the following function. Return the result directly.
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))

# Implement the following function. Return the result directly.
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], find_min