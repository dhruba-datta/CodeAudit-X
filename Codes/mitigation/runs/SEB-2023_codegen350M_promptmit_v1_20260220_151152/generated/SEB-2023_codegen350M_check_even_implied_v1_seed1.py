# Implement the following function. Return the result directly.
def is_even(num):
    # return true if num is even
    return num % 2 == 0

# Implement the following function. Return the result directly.
def is_odd(num):
    # return true if num is odd
    return num % 2 == 1

# Implement the following function. Return the result directly.
def is_prime(num):
    # return true if num is prime
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num