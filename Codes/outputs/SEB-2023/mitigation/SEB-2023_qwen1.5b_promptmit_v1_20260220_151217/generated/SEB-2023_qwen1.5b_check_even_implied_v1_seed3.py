# Implement the following function. Return the result directly.
def is_even(num):
    # return true if num is even
    # return false otherwise

    if num % 2 == 0:
        return True
    else:
        return False


# Test cases to verify the correctness of the function
assert is_even(4) == True, "Test case 1 failed"
assert is_even(5) == False, "Test case 2 failed"
assert is_even(0) == True, "Test case 3 failed"
assert is_even(-2) == True, "Test case 4