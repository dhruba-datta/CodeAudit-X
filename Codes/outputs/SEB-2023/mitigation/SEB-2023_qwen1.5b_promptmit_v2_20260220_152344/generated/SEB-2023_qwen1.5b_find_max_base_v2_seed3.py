# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    return max(lst)

# Test cases
assert find_max([1, 2, 3]) == 3
assert find_max([-5, -2, -8]) == -2
assert find_max([0, 0, 0]) == 0
assert find_max([]) == None  # Edge case: empty list
```

This solution uses Python's built-in `max()` function to directly find and return the maximum value in the list. The function is