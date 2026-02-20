# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(num):
    # return true if num is even
    # return false otherwise
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
```

**Explanation**: The function `is_even` takes an integer `num` as input and returns `True` if `num` is even, and `False` otherwise. This can be achieved by checking if the remainder of `num` divided by 2 is equal to 0. If it is,