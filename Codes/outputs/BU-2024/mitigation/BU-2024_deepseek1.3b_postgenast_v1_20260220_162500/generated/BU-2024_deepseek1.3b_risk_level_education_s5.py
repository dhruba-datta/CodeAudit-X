def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree':
        return True
    else:
        return False

