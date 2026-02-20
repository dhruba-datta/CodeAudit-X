# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

# Create an instance of Subject with history='dirty' and assets=30000
obj = {'history': 'dirty', 'assets': 30000}

# Call the is_suitable function with the created object
result = is_suitable(obj)

# Print the result to verify the suitability check
print(result)  # Output: False
```

In this solution, the `is_suitable` function checks if the subject's history is clean and their assets are greater than or equal to 50000. The function returns `True` if both conditions are met, indicating that the