# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Subject(history='clean', assets=50000)))  # Returns: True
print(is_suitable(Subject(history='dirty', assets=50000)))  # Returns: False
print(is_suitable(Subject(history='clean', assets=45000)))  # Returns: True
print(is_suitable(Subject(history='dirty', assets=45001)))  # Returns: False
print(is_suitable(Subject(history='