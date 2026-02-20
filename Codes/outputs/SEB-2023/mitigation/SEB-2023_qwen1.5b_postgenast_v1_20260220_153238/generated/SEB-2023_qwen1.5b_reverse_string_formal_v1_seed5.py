# Implement the following function. Return the result directly.
Write a Python function to reverse a string.
def reverse_string(s):
    return s[::-1]

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("world"))  # Output: "dlrow"
print(reverse_string(""))      # Output: ""
print(reverse_string("a"))     # Output: "a"