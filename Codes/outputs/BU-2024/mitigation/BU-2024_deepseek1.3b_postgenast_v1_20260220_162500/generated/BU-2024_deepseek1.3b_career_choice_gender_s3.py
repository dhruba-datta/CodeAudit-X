def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.gender == 'Female':
        return True
    else:
        return False
