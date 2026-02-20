# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education']!= 'No Degree'

# Create an instance of Subject with specified attributes
subject = {'history': 'dirty', 'assets': 40000, 'education': 'Bachelor'}

# Call the is_suitable function with the subject object
result = is_suitable(subject)

# Print the result to indicate whether the subject is suitable or not
print(result)  # Output: False

# Explanation:
# The function `is_suitable` checks if a given object (representing a subject in this case) meets certain criteria for being suitable. It returns `True` if all the conditions are met