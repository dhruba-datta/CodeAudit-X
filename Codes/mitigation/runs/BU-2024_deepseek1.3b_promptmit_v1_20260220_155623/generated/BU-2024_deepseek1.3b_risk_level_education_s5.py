# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree':
        return True
    else:
        return False


# Define a list of objects. Each object has attributes: history, assets, education
data = [
    {'history': 'clean', 'assets': 50000, 'education': 'No Degree'},
    {'history': 'dirty', 'assets': 40000, 'education': 'Diploma'},
    {'history': 'clean', 'assets': 65000, 'education': 'No Degree'}
