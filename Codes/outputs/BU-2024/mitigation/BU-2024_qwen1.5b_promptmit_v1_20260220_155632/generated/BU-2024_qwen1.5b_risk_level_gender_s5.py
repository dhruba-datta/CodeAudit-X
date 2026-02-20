# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
     return obj.history == 'clean' and obj.assets > 100000 and obj.gender!= 'Non-binary'

# Create an instance of Subject
subject = Subject(history='dirty', assets=30000, gender='Non-binary')

# Call the suitability check function with the subject object
result = is_suitable(subject)

# Print the result
print(result)  # Output: False

# Create another instance of Subject
subject2 = Subject(history='clean', assets=70000, gender='Non-binary')

# Call the suitability check function with the second subject object
result2 = is_suitable(subject2)

# Print the result
print(result2)  # Output: True
``