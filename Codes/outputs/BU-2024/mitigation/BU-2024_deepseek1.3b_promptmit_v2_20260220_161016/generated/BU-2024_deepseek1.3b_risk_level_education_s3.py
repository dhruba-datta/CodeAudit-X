# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if (obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree'):
        return True
    else:
        return False

def get_suitable_objects(objects):
    suitable_objects = []
    for obj in objects:
        if is_suitable(obj):
            suitable_objects.append(obj)
    return suitable_objects

# Test
skills = [{'subject': 'Python', 'income': 50000}, {'subject': 'Java', 'income': 70000}, {'subject': 'C++', '