# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(num):
    # return true if num is even
    return num % 2 == 0

# DO NOT TOUCH OR ALTER THE CODE BELOW
def is_odd(num):
    # return true if num is odd
    return num % 2 == 1

# Write your is_even function here:
def is_even_or_odd(num):
    # return true if num is even
    return is_even(num) or is_odd(num)

# Uncomment these