# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
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


# Implement the check_experience function. Return a boolean.
def check_experience(obj):
    # Check if the experience is greater than 50
    if obj.experience >= 50:
        return True