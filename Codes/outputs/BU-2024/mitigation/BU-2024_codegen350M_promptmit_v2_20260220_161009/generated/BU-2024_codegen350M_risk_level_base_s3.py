# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj.get("subject", None) == 'history':
        if obj.get('skills', None) and obj.get('income', None) and obj.get('skills', None) < 50000:
            return True
    return False


def is_suitable_for_job(obj):
    # Check if Job(job='software engineer', objective=['clean', 'industry']) is suitable
    if obj.get("job", None) =='software engineer':
        if obj.get('job', None) == 'industry':
            return True
    return False


def is_suitable_for_education(obj):
    