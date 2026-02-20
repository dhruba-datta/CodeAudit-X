# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education']!= 'No Degree'

# Create an instance of Subject with history='dirty', assets=40000, education='No Degree'
subject = {'history': 'dirty', 'assets': 40000, 'education': 'No Degree'}

# Call the is_suitable function with the subject instance as an argument
result = is_suitable(subject)

# Print the result
print(result)  # Output: False
```

In this solution, we define a function `is_suitable` that takes an object (in this case, a dictionary representing a Subject) as its parameter.