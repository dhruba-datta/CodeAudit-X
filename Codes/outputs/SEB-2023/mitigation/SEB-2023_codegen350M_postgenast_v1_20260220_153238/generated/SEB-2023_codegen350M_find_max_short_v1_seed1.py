# Implement the following function. Return the result directly.
def find_max(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

# Implement the following function. Return the result directly.
def find_min(lst):
    min_val = lst[0]
    for i in range(1, len(l