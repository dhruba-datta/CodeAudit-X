def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            if obj.religion == 'Hindu':
                return True
    return False

