# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if isinstance(obj, Subject):
        if (obj.history == 'clean'):
            return False
        elif (obj.assets == 50000):
            return True

# Implement the check_for_attributes function. Return a boolean.
def check_for_attributes(obj):
    # Check if an object has the required attributes
    if (obj.name!= None and obj.history!= None and obj.assets!= None):
        if (obj.name.lower()!='suicide'):
            return False
        if (obj.assets < 0):
            return False
        if (obj.assets > 50000):
            return False