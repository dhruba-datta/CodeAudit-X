# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to reverse a string.
def reverse_string(s):
    return s[::-1]

# Test cases
print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
print(reverse_string("Python"))  # Output: nohtyP
print(reverse_string("1234567890"))  # Output: 0987654321
print(reverse_string("")) 