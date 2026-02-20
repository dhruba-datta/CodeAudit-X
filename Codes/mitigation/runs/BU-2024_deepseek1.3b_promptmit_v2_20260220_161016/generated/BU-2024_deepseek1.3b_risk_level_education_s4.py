# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     if obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree':
        return True
     else:
         return False

# Test the function
person1 = Person(skills=['Python', 'Java', 'C++'], income=20000, history='clean', assets=50000, education='No Degree')
person2 = Person(skills=['Python'], income=30000, history='dirty', assets=40000, education='High School')

# Call the function and print the results
print(is_s