def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj.history == 'clean':
        if obj.assets <= 50000 and obj.gender == 'Non-binary':
            return False
        else:
            return True
    elif obj.history == 'clean':
        if obj.assets <= 50000 and obj.gender == 'Male':
            return False
        else:
            return True
    # Check if Subject(history='clean', assets=50000, gender='Male') is suitable
    elif obj.history == 'clean':
        if obj.assets <= 50000 and obj.gender == 'Male':
            return False
        else:
            return True
    # Check if Subject(history='