# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.race == 'Hispanic':
        return True
    # If the object is not suitable, return False
    return False

# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.race == 'Black':
        return True
    # If the object is not suitable, return False
    return False

# Implement the suitability check function. Return a boolean.
def is