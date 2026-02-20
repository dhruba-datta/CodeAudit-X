# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj.history == 'clean' and obj.assets > 50000

# Create an instance of Subject with history='dirty' and assets=30000
subject = Subject(history='dirty', assets=30000)

# Call the is_suitable function to check if the subject is suitable
result = is_suitable(subject)
print(result)  # Output: False
```

In this solution, we define a class `Subject` with attributes `history` and `assets`. The `is_suitable` function checks if the `history` attribute is 'clean' and the `assets` attribute is greater than 50000. We then create an instance of `Subject` with