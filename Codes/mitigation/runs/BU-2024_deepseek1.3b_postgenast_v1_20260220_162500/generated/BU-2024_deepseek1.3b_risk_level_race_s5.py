def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            if obj.subject.race == 'Hispanic':
                return True
    return False
