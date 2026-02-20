def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American':
        return True
    return False
