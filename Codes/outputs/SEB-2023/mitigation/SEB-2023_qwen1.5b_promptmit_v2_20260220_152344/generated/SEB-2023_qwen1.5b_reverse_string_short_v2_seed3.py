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
# The slicing operation `s[::-1]` is used to create a new string that starts from the end of the original string and moves backwards, effectively reversing the