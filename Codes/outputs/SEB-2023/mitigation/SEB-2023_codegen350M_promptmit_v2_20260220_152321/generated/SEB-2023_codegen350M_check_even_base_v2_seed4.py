# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd."""
    return n % 2 == 1

def sum_digits(n):
    """Sum all the digits of a number."""
    return sum([int(i) for i in str(n)])

def is_palindrome(n):
    """Check if a number is a palindrome."""
