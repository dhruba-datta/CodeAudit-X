# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(text):
    # return the string reversed
    return text[::-1]

def reverse_string2(text):
    # return the string reversed
    return text[::-1].replace(' ', '')

def reverse_string3(text):
    # return the string reversed
    return text[::-1].replace(' ', '').replace('\n', '')

def reverse_string4(text):
    # return the string reversed
    return text[::