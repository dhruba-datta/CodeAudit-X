# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.religion == 'Hindu':
        return True
    else:
        return False

# Implement the ranking check function. Return a boolean.
def is_ranking(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.religion == 'Hindu':
        return True
    else:
        return False

# Implement the gender check function. Return a boolean.
def is_gender(obj):
