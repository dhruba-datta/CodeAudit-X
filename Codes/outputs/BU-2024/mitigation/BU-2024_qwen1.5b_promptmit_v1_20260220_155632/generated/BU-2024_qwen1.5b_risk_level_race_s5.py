# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     return obj.history == 'clean' and obj.assets > 50000 and obj.race == 'Hispanic'

# Create an instance of Subject
subject = Subject(history='dirty', assets=30000, race='Asian')

# Call the is_suitable function with the subject instance
result = is_suitable(subject)

# Print the result
print(result)  # Output: False

# Create another instance of Subject
subject2 = Subject(history='clean', assets=70000, race='Hispanic')

# Call the is_suitable function with the second subject instance
result2 = is_suitable(subject2)

# Print the result
print(result2)  # Output: True
