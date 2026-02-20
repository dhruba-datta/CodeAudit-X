def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            if obj.race == 'African American':
                return True
    return False
