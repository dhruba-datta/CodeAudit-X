# Implement the following function. Return the result directly.
Write a Python function to check if an integer is even.
def is_even(n):
    # Check if the number is divisible by 2
    return n % 2 == 0

# Test cases
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
print(is_even(-6)) # Output: True
print(is_even(0))   # Output: True
```

In this solution, the function `is_even` takes an integer `n` as input and returns `True` if `