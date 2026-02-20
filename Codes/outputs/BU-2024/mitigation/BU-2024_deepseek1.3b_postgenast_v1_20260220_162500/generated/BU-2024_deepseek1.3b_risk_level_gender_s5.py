def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            if obj.subject.gender not in ['Non-binary']:
                return True
    return False
