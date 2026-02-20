# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    """Reverse a string."""
    return s[::-1]  # Using slicing to reverse the string

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
```

This solution leverages Python's powerful slicing feature to reverse a string in a single line, making it both concise and efficient. The slicing `s[::-1]` starts from the end of the string (`-1`) and moves backwards by one step at a time (`::1`). This method is highly readable and leverages