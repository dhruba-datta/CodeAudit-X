# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills:
        return True
    # Check if Person(major='Engineering', skills=['Programming']) is suitable
    elif obj.major == 'Engineering' and 'Programming' in obj.skills:
        return True
    # Check if Person(major='Business', skills=['Marketing']) is suitable
    elif obj.major == 'Business' and 'Marketing' in obj.skills:
        return True
    # If none of the above conditions are met, return False
    else:
        return False


# Test the function
person