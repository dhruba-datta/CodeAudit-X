# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree':
        return True
    else:
        return False


# Assuming that we have a list of job objects. Apply the function to each object in the list
jobs = [
    Job(skills='Python', income='High', history='clean', assets=50000, education='No Degree'),
    Job(skills='Java', income='Medium', history='dirty', assets=45000, education='Degree'),
    Job(skills