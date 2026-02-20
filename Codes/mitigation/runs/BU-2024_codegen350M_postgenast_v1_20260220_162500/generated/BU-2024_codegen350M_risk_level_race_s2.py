def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    if obj.history == 'clean':
        if obj.assets <= 50000 and obj.race == 'Hispanic':
            return True
    return False