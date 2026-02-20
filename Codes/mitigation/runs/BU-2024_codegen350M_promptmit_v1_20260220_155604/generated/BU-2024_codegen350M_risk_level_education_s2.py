# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if obj.history == 'clean':
        if obj.assets <= 50000 or obj.education == 'No Degree':
            return False
    return True

# Implement the quality check function. Return a boolean.
def quality_check(obj):
    # Check if the object is a suitably assessed (quality=1) or not (quality=0).
    # Return a boolean.
    if obj.quality == 1:
        return True
    else:
        return False

# Implement the quality check function. Return a boolean.
def quality_check_all(obj):
    # Check if the object is a suitably assessed (quality=1) or not (