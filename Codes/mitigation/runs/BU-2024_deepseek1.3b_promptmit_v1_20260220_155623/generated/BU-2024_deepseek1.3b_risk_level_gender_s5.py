# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            if obj.subject.gender not in ['Non-binary']:
                return True
    return False

# Check if the object is suitable
print(is_suitable(obj))  # should print True or False


# Check if the list of objects is suitable
def is_all_suitable(list_of_objs):
    for obj in list_of_objs:
        if not is_suitable(obj):
            return False
    return True

# Check if all objects in the list