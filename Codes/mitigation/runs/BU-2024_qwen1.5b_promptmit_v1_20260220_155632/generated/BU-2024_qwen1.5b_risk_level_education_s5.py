# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj.history == 'clean' and obj.assets > 100000 and obj.education!= 'No Degree'
    
obj = Subject(history='clean', assets=50000, education='No Degree')
print(is_suitable(obj))  # Output: True

obj2 = Subject(history='dirty', assets=40000, education='No Degree')
print(is_suitable(obj2))  # Output: False

obj3 = Subject(history='clean', assets=60000, education='Master of Science')
print(is_suitable(obj3))  # Output: True

obj4 = Subject(history='dirty', assets=80000, education='Bachelor of