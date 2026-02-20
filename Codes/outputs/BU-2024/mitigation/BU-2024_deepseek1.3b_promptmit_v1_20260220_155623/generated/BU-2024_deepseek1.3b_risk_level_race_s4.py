# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     if obj.Subject.history == 'clean' and obj.Subject.assets >= 50000 and obj.Subject.race == 'Hispanic':
        return True
     else:
        return False

# Create a list of objects
objects = [
    {'Subject': {'history': 'clean', 'assets': 40000, 'race': 'Asian'}},
    {'Subject': {'history': 'dirty', 'assets': 55000, 'race': 'Caucasian'}},
    {'Subject': {'history': 'clean', 'assets': 60000, 'race': 'Hispan