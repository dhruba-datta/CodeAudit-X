def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Reading']:
            return True
        else:
            return False
    else:
        return False

