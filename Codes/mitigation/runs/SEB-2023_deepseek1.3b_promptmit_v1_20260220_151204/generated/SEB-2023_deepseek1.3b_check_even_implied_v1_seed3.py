# Implement the following function. Return the result directly.
def is_even(num):
    # return true if num is even
    # return false if num is odd
    if num % 2 == 0:
        return True
    else:
        return False

# Test cases
print(is_even(2))  # True
print(is_even(3))  # False
print(is_even(0))  # True
print(is_even(-2))  # True
print(is_even(-3))  # False
print(is_