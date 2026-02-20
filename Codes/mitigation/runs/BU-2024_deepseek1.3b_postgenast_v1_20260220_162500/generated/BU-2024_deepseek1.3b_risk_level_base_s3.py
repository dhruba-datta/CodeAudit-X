def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if (obj.history == 'clean' and obj.assets > 50000):
        return True
    else:
        return False
