def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            return True
    return False
