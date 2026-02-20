def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if isinstance(obj, Subject):
        if (obj.history == 'clean'):
            return False
        elif (obj.assets == 50000):
            return True
