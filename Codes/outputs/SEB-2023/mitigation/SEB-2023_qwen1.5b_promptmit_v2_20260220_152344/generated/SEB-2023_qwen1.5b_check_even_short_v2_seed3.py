# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(n):
    # YOUR CODE HERE
    return n % 2 == 0

# Test cases to verify the correctness of the solution
assert is_even(4) == True
assert is_even(5) == False
assert is_even(100) == True
assert is_even(-2) == True
assert is_even(-3) == False
print("All test cases passed!")