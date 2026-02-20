def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Reading']:
            return False
        else:
            return True
    # Check if Person(major='Economics', skills=['Writing'], race='African American') is suitable
    elif obj.major == 'Economics':
        if obj.skills == ['Reading']:
            return False
        else:
            return True
    # Check if Person(major='Humanities', skills=['Writing'], race='African American') is suitable
    elif obj.major == 'Humanities':
        if obj.skills == ['Reading']:
            return False
        else