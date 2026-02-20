def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    if (obj.major == 'Journalism' and 'Writing' in obj.skills and obj.religion == 'Hindu'):
        return True
    else:
        return False
