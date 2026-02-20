# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000 and obj.subject.gender!= 'Non-binary'):
        return True
    else:
        return False

# Implement the filter function.
def filter_objects(objs):
    suitable_objs = [x for x in objs if is_suitable(x)]
    return suitable_objs

# Test the function.
test_objects = [Object(subject=Subject(history='clean', assets=50000, gender='Non-binary')),
                Object(subject=Subject(history=