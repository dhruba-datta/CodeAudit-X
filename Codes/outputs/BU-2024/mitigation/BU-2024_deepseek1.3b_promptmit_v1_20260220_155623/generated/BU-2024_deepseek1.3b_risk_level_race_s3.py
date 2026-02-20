# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    
    if (obj.history == 'clean' and obj.assets >= 50000 and obj.race == 'Hispanic'):
        return True
    else:
        return False

# Use the function.

# Create some objects:
obj1 = Object('history', 'assets', 'race')
obj2 = Object('clean', 55000, 'Hispanic')
obj3 = Object('dirty', 40000, 'Asian')

# Test the function:
print(is_suitable(obj1))  # Output: True
print(is_suitable(obj2))