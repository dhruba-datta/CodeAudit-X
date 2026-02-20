def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj.history == 'clean':
        if obj.assets <= 50000:
            return True
        else:
            return False
    # Check if Asset(history='clean', assets=50000) is suitable
    elif obj.history == 'assets':
        if obj.assets <= 50000:
            return True
        else:
            return False
    # Check if Asset(history='clean', assets=50000) is suitable
    else:
        if obj.assets <= 50000:
            return True
        else:
            return False

