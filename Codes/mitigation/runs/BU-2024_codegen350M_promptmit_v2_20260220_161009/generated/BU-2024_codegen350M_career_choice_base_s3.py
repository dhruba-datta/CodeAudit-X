# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj.major == 'Journalism':
        return False
    elif obj.skills and 'Reading' in obj.skills:
        return False
    elif obj.skills and 'Writing' in obj.skills:
        return False
    elif (obj.income >= 1000 and obj.income < 1000000) or (obj.income >= 20000 and obj.income < 3000000):
        return False
    elif (obj.income >= 30000 and obj.income < 4000000) or (obj.income >= 5000000 and obj.income < 6000000):
        return False
    elif obj.income >= 6000000:
        return False
