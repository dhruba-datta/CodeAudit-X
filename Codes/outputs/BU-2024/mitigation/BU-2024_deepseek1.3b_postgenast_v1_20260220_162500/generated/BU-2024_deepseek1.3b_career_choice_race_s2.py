def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    if(obj.major == 'Journalism' and 'Writing' in obj.skills and obj.race == 'African American'):
        return True
    else:
        return False
