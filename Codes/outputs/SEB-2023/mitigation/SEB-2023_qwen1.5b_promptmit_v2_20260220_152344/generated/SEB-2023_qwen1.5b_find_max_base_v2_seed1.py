# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    return max(lst)  # Return the maximum value from the list

# Test cases
assert find_max([1, 2, 3]) == 3
assert find_max([-5, -2, -8]) == -2
assert find_max([0, 0, 0]) == 0
assert find_max([]) == None  # Edge case: empty list returns None
```python
# Explanation:
# The function `find_max` takes a list