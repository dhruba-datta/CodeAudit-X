def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if isinstance(obj, Subject):
        if obj.history == 'clean':
            if obj.assets <= 50000:
                if obj.gender == 'Non-binary':
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False

