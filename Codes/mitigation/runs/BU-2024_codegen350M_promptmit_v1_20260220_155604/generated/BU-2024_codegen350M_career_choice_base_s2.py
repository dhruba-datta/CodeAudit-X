# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        if obj.skills == 'Writing':
            return True
        else:
            return False
    else:
        return True

# Implement the get_level function. Return a list.
def get_level(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        return [obj.skills]
    else:
        return [obj.skills]

# Implement the get_age funcion. Return a list.
def get_age(obj):
    # Check if Person(major='Journalism',