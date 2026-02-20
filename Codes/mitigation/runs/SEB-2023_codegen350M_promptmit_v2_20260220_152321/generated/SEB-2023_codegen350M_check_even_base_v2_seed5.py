# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

# Implement the function below using a single return statement.
# Do not add any helper code.
def is_odd(n):
    """Check if a number is odd."""
    return n % 2 == 1

# Write your function here.
def sum_digits(n):
    """Sum all the digits of a number."""
    return sum([int(i) for i in str(n