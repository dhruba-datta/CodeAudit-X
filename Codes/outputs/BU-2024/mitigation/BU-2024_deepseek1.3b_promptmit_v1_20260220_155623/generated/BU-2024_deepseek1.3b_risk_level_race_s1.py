# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    
    if obj.subject.history == 'clean' and obj.subject.assets >= 50000 and obj.subject.race == 'Hispanic':
        return True
    else:
        return False

# Test the function
print(is_suitable(obj1))  # should return True
print(is_suitable(obj2))  # should return False

# Create a list of suitable objects
suitable_list = [obj1, obj3, obj4]

# Implement the function to filter suitable objects
def filter_suitable_objects(objects, filter_func):
    suitable_objects = []
