# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    """Reverse a string."""
    # Your solution here
    return s[::-1]  # Using slicing to reverse the string

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
```

This solution leverages Python's powerful slicing feature to reverse the string in a single line, making it both concise and efficient. The `s[::-1]` notation means start at the end of the string (`-1`), end at position 0 (`0`), move with the step