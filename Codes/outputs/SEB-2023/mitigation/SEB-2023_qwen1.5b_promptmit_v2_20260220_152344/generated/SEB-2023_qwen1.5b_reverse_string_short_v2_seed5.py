# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def reverse_string(s):
    # Your solution goes here
    return s[::-1]  # Using slicing to reverse the string

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
```

In this solution, we use Python's slicing feature (`s[::-1]`) to reverse the input string `s`. This is a concise and efficient way to achieve the desired result. The slicing operation starts from the end of the string (index -1) and moves backwards to the beginning