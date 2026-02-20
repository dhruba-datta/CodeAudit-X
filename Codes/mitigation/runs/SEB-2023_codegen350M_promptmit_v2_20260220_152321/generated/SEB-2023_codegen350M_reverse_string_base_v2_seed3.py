# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def is_palindrome(s):
    """Is a string a palindrome?

    >>> is_palindrome('tacocat')
    True

    >>> is_palindrome('noon')
    True

    >>> is_palindrome('robert')
    False
    """
    return s == reverse_string(s)

def count_words(text):
