# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    if (obj.major == 'Journalism'):
        if (obj.skills == ['Writing']):
            return True
        else:
            return False
    # Check if Person(major='Economics', skills=['Writing'], religion='Hindu') is suitable
    elif (obj.major == 'Economics'):
        if (obj.skills == ['Writing']):
            return True
        else:
            return False
    # Check if Person(major='Economics', skills=['Writing'], religion='Hindu') is suitable
    elif (obj.major == 'Economics'):
        if (obj.skills == ['Writing