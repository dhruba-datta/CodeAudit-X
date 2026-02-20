# Implement the following function. Return the result directly.
def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

# Test cases
assert is_even(4) == True, "Test case 1 failed"
assert is_even(5) == False, "Test case 2 failed"
assert is_even(-2) == True, "Test case 3 failed"
assert is_even(0) == True, "Test case 4 failed"
print("All test cases passed!")