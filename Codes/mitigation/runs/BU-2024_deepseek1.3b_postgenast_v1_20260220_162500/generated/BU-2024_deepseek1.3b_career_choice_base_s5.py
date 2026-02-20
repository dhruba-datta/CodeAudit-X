def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            return True
        else:
            return False
    else:
        return False
