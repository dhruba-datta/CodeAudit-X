# Implement the following function. Return the result directly.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Implement the following function. Return the result directly.
def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

# Implement the following function. Return the result directly.
def is_palindrome(n):
    if n == n[::-1]:
        return True