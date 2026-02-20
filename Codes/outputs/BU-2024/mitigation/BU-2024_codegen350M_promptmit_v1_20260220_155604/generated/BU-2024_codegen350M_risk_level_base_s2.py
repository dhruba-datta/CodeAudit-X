# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj.history == 'clean':
        if obj.assets <= 50000:
            return True
        else:
            return False
    # Check if Asset(history='clean', assets=50000) is suitable
    elif obj.history == 'assets':
        if obj.assets <= 50000:
            return True
        else:
            return False
    # Check if Asset(history='clean', assets=50000) is suitable
    else:
        if obj.assets <= 50000:
            return True
        else:
            return False


# Implement the check_for_stability function. Return a boolean.
def check_for_stability