# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    return max(lst) if lst else None

# Test cases
assert find_max([1, 2, 3]) == 3
assert find_max([-5, -2, -8]) == -2
assert find_max([]) is None
assert find_max([42]) == 42
print("All test cases passed!")