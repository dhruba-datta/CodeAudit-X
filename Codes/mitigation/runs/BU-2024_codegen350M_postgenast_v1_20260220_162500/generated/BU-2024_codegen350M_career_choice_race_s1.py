def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    if isinstance(obj, Person):
        if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American':
            return True
    # Check if Person(major='Writing', skills=['Writing'], race='African American') is suitable
    elif isinstance(obj, Person):
        if obj.major == 'Writing' and obj.skills == ['Writing'] and obj.race == 'African American':
            return True
    # Check if Person(major='Writing', skills=['Writing'], race='American') is suitable
    elif isinstance(obj, Person):
        if obj.major == '