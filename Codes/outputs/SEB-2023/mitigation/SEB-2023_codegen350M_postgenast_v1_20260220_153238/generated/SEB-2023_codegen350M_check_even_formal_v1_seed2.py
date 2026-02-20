# Implement the following function. Return the result directly.
Write a Python function to check if an integer is even.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Test your function.
# Should return True.
print(is_even(3))
# Should return False.
print(is_even(5))
# Should return True.
print(is_even(6))
# Should return False.
print(is_even(7))
# Should return True.
print(is_even(