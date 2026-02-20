# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Subject(history='clean', assets=50000, gender='Non-binary')))  # Should return True
print(is_suitable(Subject(history='dirty', assets=50000, gender='Non-binary')))  # Should return False
print(is_suitable(Subject(history='clean', assets=40000, gender='Non-binary')))  # Should return False
print(is_suitable(Subject(history='clean', assets=50