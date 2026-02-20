def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    # for the given object.
    if obj.history == "clean":
        if obj.assets > 50000 or obj.education == "No Degree":
            return False
    return True

