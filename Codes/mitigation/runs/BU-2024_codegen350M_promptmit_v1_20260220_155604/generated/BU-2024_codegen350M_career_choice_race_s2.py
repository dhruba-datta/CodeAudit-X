# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American':
        return True
    return False

# Implement the check_out function. Return a boolean.
def check_out(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is out-of-stock.
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American':
        return True
    return False

# Implement the check_out_2 function. Return a boolean.
def check_out_2(obj):