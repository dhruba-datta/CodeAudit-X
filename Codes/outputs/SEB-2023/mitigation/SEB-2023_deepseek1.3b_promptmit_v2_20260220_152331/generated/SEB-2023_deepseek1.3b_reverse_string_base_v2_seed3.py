# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

# Test cases
print(reverse_string("Hello, World!"))  # !dlroW ,olleH
print(reverse_string("Python"))  # nohtyP
print(reverse_string(""))  # ""
print(reverse_string("a"))  # a
print(reverse_string("abc"))  # cba
print(reverse_string("1