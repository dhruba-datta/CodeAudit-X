# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """Find the maximum element in a list."""
    return max(lst)  # Return the maximum value from the list

# Example usage:
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
print(find_max([-10, -20, -30, -40, -50]))  # Output: -10
```python
# Check function to verify the correctness of the solution
def check_solution():
    assert find_max([1,