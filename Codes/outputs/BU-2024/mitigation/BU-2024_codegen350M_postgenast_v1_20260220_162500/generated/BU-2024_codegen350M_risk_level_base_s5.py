def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    # for the suitability check.
    # Check if the object is a proper object, and if the object has
    # a '__eq__()' method.
    # If the object is not a property, or has a '__hash__' method, return False.
    if not hasattr(obj, '__eq__') or not hasattr(obj, '__hash__'):
        return False
    else:
        if not obj.__eq__(obj):
            return False
        if not isinstance(obj, Property):
            return False
        if obj.history == 'clean':
            return True
        else:
            return False
