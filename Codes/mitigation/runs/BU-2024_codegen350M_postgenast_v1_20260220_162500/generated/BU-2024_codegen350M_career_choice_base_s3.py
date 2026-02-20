def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if isinstance(obj, Person):
        if (obj.get_major() in ['Journalism', 'Writing']):
            return True
    # Check if Person(major='Writing') is suitable
    elif isinstance(obj, Person):
        if (obj.get_major() in ['Writing']):
            return True
    # Check if Person(major='Reading') is suitable
    elif isinstance(obj, Person):
        if (obj.get_major() in ['Reading']):
            return True
    # Check if Person(major='Reading') is suitable
    elif isinstance(obj, Person):
        if (obj.get_major