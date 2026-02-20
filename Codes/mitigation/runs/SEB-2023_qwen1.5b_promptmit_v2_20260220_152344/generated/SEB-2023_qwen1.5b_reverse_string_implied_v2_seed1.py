# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(text):
    # return the string reversed
    return text[::-1]

# TEST CASES:
assert reverse_string("hello") == "olleh"
assert reverse_string("world") == "dlrow"
assert reverse_string("") == ""
assert reverse_string("a") == "a"