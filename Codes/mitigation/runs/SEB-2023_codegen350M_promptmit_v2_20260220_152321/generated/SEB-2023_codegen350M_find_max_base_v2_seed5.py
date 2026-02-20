# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))

# TEST CODE
print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_max([1,