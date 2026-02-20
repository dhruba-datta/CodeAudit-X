# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to reverse a string.
def reverse_string(s):
    # Your code here
    return s[::-1]  # Using slicing to reverse the string

# Test the function with provided data points
assert reverse_string("hello") == "olleh"
assert reverse_string("world") == "dlrow"
assert reverse_string("") == ""
assert reverse_string("a") == "a"  # Edge case: single character string
print("All tests passed!")  # Output: All tests passed!