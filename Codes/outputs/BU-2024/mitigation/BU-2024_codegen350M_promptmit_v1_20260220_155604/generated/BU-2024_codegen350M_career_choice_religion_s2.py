# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.religion == 'Hindu':
        return True
    else:
        return False

# Implement the get_level function. Return a list.
def get_level(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.religion == 'Hindu':
        return 1
    else:
        return 0

# Implement the get_qualification_type function. Return a list.
def get_