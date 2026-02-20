# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to reverse a string.
def reverse_string(s):
    """
    :param s: a string
    :return: a reversed string
    """
    # TODO: Write your code here
    return s[::-1]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert reverse_string("hello") == "olleh"
    assert reverse_string("radar") == "tar