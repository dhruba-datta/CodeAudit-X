def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     if obj.Subject.history == 'clean' and obj.Subject.assets >= 50000 and obj.Subject.race == 'Hispanic':
        return True
     else:
        return False
