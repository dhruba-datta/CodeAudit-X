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
```output
True
False
```
The function `is_even` correctly returns `True` if the input number `num` is even, and `False` otherwise. The provided test cases confirm that the function works as expected. 

Here's the final implementation of the function:

```python
def