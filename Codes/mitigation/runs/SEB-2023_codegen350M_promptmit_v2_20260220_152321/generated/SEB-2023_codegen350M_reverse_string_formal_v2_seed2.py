# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to reverse a string.
def reverse_string(s):
    """
    :param s: a string
    :return: the reversed string
    """
    # TODO: Write your code here
    return s[::-1]

# These "asserts" are used for self-checking and not for testing
assert reverse_string("hello") == "olleh"
assert reverse_string("radar") == "tar"
assert reverse_string("") == ""

print("Coding