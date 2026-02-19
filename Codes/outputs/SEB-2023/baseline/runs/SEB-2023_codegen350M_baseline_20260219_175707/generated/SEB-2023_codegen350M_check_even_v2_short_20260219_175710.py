def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

def