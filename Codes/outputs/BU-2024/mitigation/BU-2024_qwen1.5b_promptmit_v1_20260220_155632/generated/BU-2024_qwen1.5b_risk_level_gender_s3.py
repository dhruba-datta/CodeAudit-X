# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['gender']!= 'Non-binary'

# Create an instance of Subject with history='dirty', assets=40000, gender='Non-binary'
subject = {'history': 'dirty', 'assets': 40000, 'gender': 'Non-binary'}

# Call the is_suitable function with the subject instance
result = is_suitable(subject)

# Print the result to verify the suitability check
print(result)  # Output: False
```

In this solution, the `is_suitable` function checks if a given object meets specific criteria for being suitable. The criteria are that the subject's