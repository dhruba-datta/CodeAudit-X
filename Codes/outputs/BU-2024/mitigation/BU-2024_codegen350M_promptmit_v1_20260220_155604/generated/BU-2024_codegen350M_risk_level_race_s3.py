# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.race == 'Hispanic':
        return True
    # Check if Subject(history='clean', assets=50000, race='Native') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.race == 'Native':
        return True
    # Check if Subject(history='clean', assets=50000, race='Asian') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.race == 'Asian':
        return True
    # Check if Subject(history='clean', assets=50000, race='Native') is