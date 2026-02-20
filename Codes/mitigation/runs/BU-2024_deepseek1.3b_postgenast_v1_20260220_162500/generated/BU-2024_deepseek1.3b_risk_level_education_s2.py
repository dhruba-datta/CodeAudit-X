def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000 and obj.subject.education == 'No Degree'):
        return True
    else:
        return False

