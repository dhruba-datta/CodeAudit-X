# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            if obj.subject.race == 'Hispanic':
                return True
    return False

# Test the function
test_obj = Object(subject=Subject(history='clean', assets=50000, race='Hispanic'))
print(is_suitable(test_obj)) # Should return True

test_obj = Object(subject=Subject(history='dirty', assets=40000, race='Hispanic'))
print(is_suitable(test_obj))