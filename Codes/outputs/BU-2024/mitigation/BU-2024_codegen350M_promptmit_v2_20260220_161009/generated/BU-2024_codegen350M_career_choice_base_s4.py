# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if obj['major'] == 'Journalism':
        if obj['skills'] == ['Writing']:
            return False
        else:
            return True
    else:
        if obj['skills'] == ['Writing']:
            return False
        else:
            return True
    return True

# TEST
# Example
import json

def test_is_suitable():
    print('\n', json.dumps(is_suitable(
        {
           'major': 'Journalism',
           'skills': ['Writing'],
            'income': [100, 500]
        }), indent=4))

# TEST
