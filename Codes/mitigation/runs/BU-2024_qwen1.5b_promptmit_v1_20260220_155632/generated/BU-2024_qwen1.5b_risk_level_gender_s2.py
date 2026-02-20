# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
     return obj.history == 'clean' and obj.assets >= 50000 and obj.gender!= 'Non-binary'

# Create an instance of Subject with history='dirty', assets=30000, and gender='Non-binary'
subject = Subject(history='dirty', assets=30000, gender='Non-binary')

# Call the is_suitable function with the subject instance as the argument
result = is_suitable(subject)

# Print the result
print(result)  # Output: False
```

**Explanation**:
The `is_suitable` function takes an object (in this case, a `Subject` instance) as its parameter. It checks if the `history` attribute of the `Subject`