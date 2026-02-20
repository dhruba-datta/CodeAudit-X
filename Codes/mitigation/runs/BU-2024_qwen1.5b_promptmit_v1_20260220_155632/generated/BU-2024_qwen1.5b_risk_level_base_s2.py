# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj.history == 'clean' and obj.assets >= 50000

# Create instances of Subject
subject1 = Subject(history='dirty', assets=40000)
subject2 = Subject(history='clean', assets=60000)

# Call the suitability check function for subject1
print(is_suitable(subject1))  # Output: False

# Call the suitability check function for subject2
print(is_suitable(subject2))  # Output: True
```

In this solution, we define a `Subject` class with attributes `history` and `assets`. The `is_suitable` function checks if a `Subject` instance meets the criteria for being suitable (i.e., `history