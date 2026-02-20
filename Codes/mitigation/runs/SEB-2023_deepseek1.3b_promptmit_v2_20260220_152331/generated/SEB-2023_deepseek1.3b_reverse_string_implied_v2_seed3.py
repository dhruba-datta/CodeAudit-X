# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(text):
    # return the string reversed
    return text[::-1]

# Test cases
print(reverse_string("Hello, World!"))  # !dlroW ,olleH
print(reverse_string("Python"))  # nohtyP
print(reverse_string("1234567890"))  # 0987654321
print(reverse_string(""))  # ""
print(re