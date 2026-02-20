# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    # for the suitability check.
    # Check if obj.major == 'Journalism'
    # Check if obj.gender == 'Female'
    # Check if obj.skills == ['Writing']
    if obj.major == 'Journalism':
        if obj.gender == 'Female':
            if obj.skills == ['Writing']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# Implement the suitability check function. Return a boolean.
def is_suitable_v2(obj):
    # Check if Person(major='Journalism', skills=['Writing'],