# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj.history == 'clean':
        if (obj.assets < 50000) or (obj.gender == 'Non-binary'):
            return False
    else:
        if obj.assets < 50000:
            return False
    return True


# Implement the suitability check function. Return a boolean.
def is_suitable_without_asset(obj):
    return not is_suitable(obj)


# Implement the suitability check function. Return a boolean.
def is_suitable_with_asset(obj):
    if is_suitable_without_asset(obj):
        return False

    if obj.asset