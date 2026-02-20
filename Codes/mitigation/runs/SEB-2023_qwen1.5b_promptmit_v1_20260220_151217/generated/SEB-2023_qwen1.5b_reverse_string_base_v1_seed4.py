# Implement the following function. Return the result directly.
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


# Test cases
assert reverse_string("hello") == "olleh"
assert reverse_string("") == ""
assert reverse_string("a") == "a"