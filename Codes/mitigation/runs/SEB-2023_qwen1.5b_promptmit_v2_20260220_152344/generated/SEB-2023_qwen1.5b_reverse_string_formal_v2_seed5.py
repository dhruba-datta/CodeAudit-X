# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to reverse a string.
def reverse_string(s):
    # Your solution here
    return s[::-1]  # Using slicing to reverse the string

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("world"))  # Output: "dlrow"
print(reverse_string(""))      # Output: ""
```

In this solution, we use Python's slicing feature to reverse the string. The slice `s[::-1]` means start at the end of the string and end at position 