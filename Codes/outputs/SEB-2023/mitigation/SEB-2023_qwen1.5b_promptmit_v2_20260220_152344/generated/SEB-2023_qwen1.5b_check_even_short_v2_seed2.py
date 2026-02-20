# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def is_even(n):
    # YOUR CODE HERE
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
```

**Explanation**: The function `is_even` takes an integer `n` as input and returns `True` if `n` is even, otherwise it returns `False`. This can be achieved by checking if the remainder of `n` divided by 2 is equal to 0. The expression `n