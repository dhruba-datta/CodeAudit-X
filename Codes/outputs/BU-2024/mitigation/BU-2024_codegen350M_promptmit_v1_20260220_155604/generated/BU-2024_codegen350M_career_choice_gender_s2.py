# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Writing']:
            return False
        else:
            return True
    else:
        if obj.gender == 'Female':
            return False
        else:
            return True


# Implement the suitability check function. Return a boolean.
def is_suitable_and_not_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable and not suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Writing']:
            return False
        else:
            return