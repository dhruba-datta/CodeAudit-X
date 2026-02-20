# Implement the following function. Return the result directly.
def is_even(n):
    # Write your code here
    return n % 2 == 0


# Test cases to verify the correctness of the function
assert is_even(4) == True, "Test case 1 failed"
assert is_even(5) == False, "Test case 2 failed"
assert is_even(0) == True, "Test case 3 failed"
assert is_even(-2) == True, "Test case 4 failed"
assert is_even(1) == False