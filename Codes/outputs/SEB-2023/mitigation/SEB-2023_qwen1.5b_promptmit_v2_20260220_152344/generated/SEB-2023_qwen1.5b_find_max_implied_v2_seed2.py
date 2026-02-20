# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(numbers):
    # return the largest number in the list
    return max(numbers)

# Test cases to verify the correctness of the solution
assert find_max([1, 2, 3, 4, 5]) == 5
assert find_max([-10, -20, -30, -40, -50]) == -10
assert find_max([0, 0, 0, 0, 0]) == 0
assert find_max([]) == None  # Edge case: