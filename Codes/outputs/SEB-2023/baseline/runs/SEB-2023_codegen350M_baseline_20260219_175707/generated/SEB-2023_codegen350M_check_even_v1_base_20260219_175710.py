def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd."""
    return n % 2 == 1

def sum_numbers(n):
    """Sum all numbers from 0 to n."""
    return n + sum(range(n))

def factorial(n):
    """Calculate factorial of n."""
    return 1 if n == 0 else n * fact