# Implement the following function. Return the result directly.
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

# Test the function
print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
print(reverse_string("Python"))  # Output: nohtyP
print(reverse_string("1234567890"))  # Output: 0987654321
print(reverse_string(""))