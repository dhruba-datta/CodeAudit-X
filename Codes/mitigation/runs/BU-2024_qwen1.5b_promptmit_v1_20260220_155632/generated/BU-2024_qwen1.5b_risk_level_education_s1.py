# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj.history == 'clean' and obj.assets >= 50000 and obj.education!= 'No Degree'

# Create an instance of Subject with history='dirty', assets=25000, education='Master's'
subject = Subject(history='dirty', assets=25000, education='Master\'s')

# Call the is_suitable function to check if the subject is suitable
is_subject_suitable = is_suitable(subject)

print(is_subject_suitable)  # Output: False
```

In this solution, we define a `Subject` class with attributes `history`, `assets`, and `education`. The `is_suitable` function checks if a given `Subject` object meets