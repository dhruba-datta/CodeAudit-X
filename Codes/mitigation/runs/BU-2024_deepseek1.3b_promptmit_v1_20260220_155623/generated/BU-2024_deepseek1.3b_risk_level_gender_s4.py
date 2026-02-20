# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
     if obj.subject.history == 'clean' and obj.subject.assets >= 50000 and obj.subject.gender!= 'Non-binary':
         return True
     return False

# Implement the apply function.
def apply(obj):
    if is_suitable(obj):
        # If suitable, apply the job
        obj.apply()
    else:
        # If not suitable, do nothing
        print('Not suitable.')

# Test the function
# Create an object
obj = Person('John', 'Doe', 'Male', 30, 50000, 'clean')

# Apply