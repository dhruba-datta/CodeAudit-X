# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    """Reverse the string s.

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Hi!")
    'Hii!'
    >>> reverse_string("  ")
    ''
    >>> reverse_string("")
    ''
    """
    # YOUR CODE HERE
    return s[::-1]

# Check correctness of your solution
print('solution 1:', reverse_