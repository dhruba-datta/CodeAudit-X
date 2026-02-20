def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    # for the suitability check.
    # Check if the person is a Singer, a Writer, a Person, or a Person in a race.
    if isinstance(obj, Person):
        if obj.major == 'Singer':
            return False
        if obj.major == 'Writer':
            return False
        if obj.race == 'African American':
            return False
    # Check if the person is a Singer in a race.
    if isinstance(obj, Singer):
        return False
    # Check if the person is a Singer in a race in a race.
    if isinstance(obj, Writer):
        return False
    # Check if the