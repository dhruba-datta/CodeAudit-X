# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    if (obj.history == 'clean' and obj.assets >= 50000 and obj.gender!= 'Non-binary'):
        return True
    else:
        return False

# Create a list of people
people = [Person(history='clean', assets=50000, gender='Non-binary'),
          Person(history='dirty', assets=40000, gender='Non-binary'),
          Person(history='messy', assets=30000, gender='Non-binary'),
          Person(history='clean', assets=45000, gender=