# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj.history == 'clean' and obj.assets > 100000 and obj.education!= 'No Degree'
     
# Create an instance of Subject with history='dirty', assets=30000, education='Bachelor's'
subject = Subject(history='dirty', assets=30000, education='Bachelor's')

# Call the is_suitable function with the subject instance as an argument
result = is_suitable(subject)

# Print the result to verify the output
print(result)  # Output: False
```

In this solution, the `is_suitable` function checks if a given `Subject` object meets certain criteria. It returns `True` if all conditions are met, otherwise