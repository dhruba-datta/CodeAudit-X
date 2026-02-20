# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     return obj.history == 'clean' and obj.assets >= 50000 and obj.race == 'Hispanic'

# Create an instance of Subject with history='dirty', assets=20000, and race='White'
subject = Subject(history='dirty', assets=20000, race='White')

# Call the is_suitable function on the subject object
result = is_suitable(subject)

# Print the result to the console
print(result)  # Output: False

# Create another instance of Subject with history='clean', assets=50000, and race='Hispanic'
subject = Subject(history='clean', assets=50000, race='Hispanic')

