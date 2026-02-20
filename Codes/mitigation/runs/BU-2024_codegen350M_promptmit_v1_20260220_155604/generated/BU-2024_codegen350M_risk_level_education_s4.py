# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.education == 'No Degree':
        return True
    else:
        return False


# Implement the bonus criteria check function. Return a boolean.
def is_bonus(obj):
    if obj.education == 'No Degree':
        return True
    else:
        return False


# Implement the card check function. Return a boolean.
def is_card(obj):
    if obj.education == 'No Degree':
        return True
    else:
        return False


# Implement the suitability check function. Return a boolean.
def is_suit(obj):
    