# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(n):
    # YOUR CODE HERE
    return n % 2 == 0

# Test cases to verify the correctness of your solution
assert is_even(4) == True, "Test case 1 failed"
assert is_even(5) == False, "Test case 2 failed"
assert is_even(0) == True, "Test case 3 failed"
assert is_even(-2) == True, "Test case 4 failed"
assert is_even(-1) == False,