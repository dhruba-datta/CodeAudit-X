def is_even(num):
    # return true if num is even
    # return false if num is odd
    return num % 2 == 0

def is_odd(num):
    # return true if num is odd
    # return false if num is even
    return num % 2 == 1

def sum_digits(num):
    # return sum of digits in num
    # return 0 if num is 0
    # return 1 if num is 1
    return sum(int(i) for i in