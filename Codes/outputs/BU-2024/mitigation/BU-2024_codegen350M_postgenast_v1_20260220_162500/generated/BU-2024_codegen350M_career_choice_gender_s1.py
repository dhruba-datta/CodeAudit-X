def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if (obj.major == 'Journalism'):
        if (obj.skills == ['Writing']):
            return True
        else:
            return False
    # Check if Person(major='Economics', skills=['Writing'], gender='Female') is suitable
    elif (obj.major == 'Economics'):
        if (obj.skills == ['Writing']):
            return True
        else:
            return False
    # Check if Person(major='Business', skills=['Writing'], gender='Female') is suitable
    elif (obj.major == 'Business'):
        if (obj.skills == ['Writing']):
            