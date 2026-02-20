# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     if obj.subject.history == 'clean' and obj.subject.assets >= 50000:
        return True
     else:
         return False

# Check if all objects in the list are suitable
def check_all_suitability(obj_list):
    for obj in obj_list:
        if not is_suitable(obj):
            return False
    return True

# Test the function
company = Company(name='Company1', subjects=[Subject(history='clean', assets=50000), Subject(history='dirty', assets=30000)], location='USA')
