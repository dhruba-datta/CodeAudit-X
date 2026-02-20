# Implement the following function. Return the result directly.
def find_max(lst):
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

# Implement the following function. Return the result directly.
def find_min(lst):
    min_value = lst[0]
    for i in range(1, len(l