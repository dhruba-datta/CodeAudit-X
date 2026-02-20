# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if isinstance(obj, Subject):
        if obj.history == 'clean':
            if obj.assets <= 50000:
                return True
            else:
                return False
        else:
            return False
    return False

# Implement the quality check function. Return a boolean.
def is_qualier(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if isinstance(obj, Subject):
        if obj.history == 'clean':
            if obj.assets <= 50000:
                return True
            else:
                return False
        else:
            return False
    return False

# Implement