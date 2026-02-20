# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to check if an integer is even.
def is_even(n):
    # Your code here
    pass

# Test cases
assert is_even(4) == True
assert is_even(5) == False
assert is_even(0) == True
assert is_even(-2) == True
assert is_even(-1) == False
```
```python
def is_even(n):
    return n % 2 == 0
```python
def is_even(n):
    return n & 1 == 0
```python
def