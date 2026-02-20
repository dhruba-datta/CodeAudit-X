# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        if obj.skills == 'Writing':
            return True
        else:
            return False
    else:
        return True

def is_suitable_for_credit(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        if obj.skills == 'Reading':
            return True
        else:
            return False
    else:
        return True

def is_suitable_for_credit_with_tax(obj):
    # Check if Person(major='Journalism', skills=['Writing