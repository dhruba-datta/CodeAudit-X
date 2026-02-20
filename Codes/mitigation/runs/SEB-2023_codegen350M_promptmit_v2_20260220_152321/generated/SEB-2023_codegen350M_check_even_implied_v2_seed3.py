# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(num):
    # return true if num is even
    return num % 2 == 0

def is_prime(num):
    # return true if num is a prime number
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_prime_number(num):
    # return true if num is a prime number
    for i in range(2, num):
        if num % i == 0:
            return