# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    # Your solution goes here
    return max(lst) if lst else None

# Test cases to verify the correctness of your implementation
assert find_max([1, 2, 3, 4, 5]) == 5
assert find_max([-1, -2, -3, -4, -5]) == -1
assert find_max([]) == None
assert find_max([0]) == 0
print("All test cases passed!")