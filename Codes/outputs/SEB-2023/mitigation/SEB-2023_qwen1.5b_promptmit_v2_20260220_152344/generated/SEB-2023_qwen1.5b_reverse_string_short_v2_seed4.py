# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    # Your solution goes here
    return s[::-1]  # Using slicing to reverse the string

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
```python
# Explanation:
# The function `reverse_string` takes a string `s` as input and returns its reverse. 
# This is achieved by using Python's slicing feature, which allows us to create a new string that is a copy of the original string but in reverse order. The