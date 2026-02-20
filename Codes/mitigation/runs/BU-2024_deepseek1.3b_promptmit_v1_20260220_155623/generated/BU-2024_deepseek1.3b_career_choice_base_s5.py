# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            return True
        else:
            return False
    else:
        return False

# Implement the filter function.
def filter(objects, is_suitable_func):
    suitable_objects = []
    for obj in objects:
        if is_suitable_func(obj):
            suitable_objects.append(obj)
    return suitable_objects

# Test the functions
persons = [Person('John', 'Journalism', ['Writing', 'Reading']), 
           Person('Emma', 'Marketing