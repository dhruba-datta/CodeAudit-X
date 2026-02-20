def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj.history == 'clean':
        if (obj.assets < 50000):
            return False
        else:
            return True
    # Check if Subject(history='clean', assets=10000) is suitable
    elif obj.history == 'clean':
        if (obj.assets < 10000):
            return False
        else:
            return True
    # Check if Subject(history='clean', assets=50000) is suitable
    elif obj.history == 'clean':
        if (obj.assets < 50000):
            return False
        else:
            return True
    # Check if Subject(history='clean', assets=10000) is suitable