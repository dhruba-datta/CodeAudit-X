# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to check if an integer is even.
def is_even(n):
    return n % 2 == 0

# Test cases
print(is_even(2))  # True
print(is_even(3))  # False
print(is_even(0))  # True
print(is_even(-2))  # True
print(is_even(-3))  # False
print(is_even(100))  # False
print(is_even(-100))  #