# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

# Create an instance of Subject with history='dirty' and assets=20000
subject = {'history': 'dirty', 'assets': 20000}

# Call the is_suitable function with the subject instance as an argument
result = is_suitable(subject)

# Print the result of the suitability check
print(result)  # Output: False
```

In this solution, the `is_suitable` function checks if the `Subject` object has a `history` attribute equal to 'clean' and an `assets` attribute greater than or equal to 50000. The