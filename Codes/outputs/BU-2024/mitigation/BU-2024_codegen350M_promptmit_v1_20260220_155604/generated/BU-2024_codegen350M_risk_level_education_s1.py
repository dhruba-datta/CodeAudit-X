# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if isinstance(obj, Subject):
        if obj.history == 'clean':
            if obj.assets <= 50000 and obj.education == 'No Degree':
                return True
            else:
                return False
        else:
            return False
    # Check if Subject(history='clean', assets=50000, education='Graduate') is suitable
    elif isinstance(obj, Subject):
        if obj.history == 'clean':
            if obj.assets <= 50000 and obj.education == 'Graduate':
                return True
            else:
                return False
        else:
            return False
    # Check if Subject(history='clean', assets