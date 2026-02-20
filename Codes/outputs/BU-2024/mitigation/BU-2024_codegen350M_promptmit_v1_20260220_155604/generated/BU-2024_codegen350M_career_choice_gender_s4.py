# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Reading']:
            return True
        else:
            return False
    else:
        return False


# Implement the check_skill_level function. Return a boolean.
def check_skill_level(obj):
    # Check if the skill level is greater than 10
    if obj.skills > 10:
        return True
    else:
        return False


# Implement the check_gender function. Return a boolean.
def check_gender(obj):
    # Check if the gender is 'Male' or 'Female'
    if obj.gender == 'Male':
        