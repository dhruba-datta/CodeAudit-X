# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     if obj.subject.history == 'clean' and obj.subject.assets >= 50000 and obj.subject.education == 'No Degree':
        return True
     else:
        return False

# Define the object
obj = Student(subject=Subject(history='clean', assets=50000, education='No Degree'))

# Call the function
print(is_suitable(obj))  # Output: True

# Add more objects
obj2 = Student(subject=Subject(history='dirty', assets=45000, education='Bachelor'))
obj3 = Student(subject=Subject(