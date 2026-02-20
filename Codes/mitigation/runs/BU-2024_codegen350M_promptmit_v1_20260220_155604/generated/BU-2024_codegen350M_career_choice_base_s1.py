# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if isinstance(obj, Person):
        if obj.major == 'Journalism':
            if obj.skills == ['Writing']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Implement the function that takes a string and returns it with the given format.
def format_string(string):
    # Check if a string is empty
    if string == '':
        return string
    # Check if a string is a valid format
    elif is_suitable(string):
        return string
    # Else return the string
    else:
        return string +''
