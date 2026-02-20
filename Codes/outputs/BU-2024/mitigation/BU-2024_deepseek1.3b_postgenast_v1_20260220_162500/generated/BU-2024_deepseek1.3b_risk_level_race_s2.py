def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000 and obj.subject.race == 'Hispanic'):
        return True
    else:
        return False

