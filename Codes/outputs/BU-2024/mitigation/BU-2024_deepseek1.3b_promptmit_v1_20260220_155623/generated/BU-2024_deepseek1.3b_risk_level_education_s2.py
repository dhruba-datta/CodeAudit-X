# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000 and obj.subject.education == 'No Degree'):
        return True
    else:
        return False


# Implement the filter function.
def filter_suitable_objects(objects):
    suitable_objects = []
    for obj in objects:
        if is_suitable(obj):
            suitable_objects.append(obj)
    return suitable_objects

# Test the function.
test_objects = [
    Object(subject=Subject(history='clean', assets=45000, education=