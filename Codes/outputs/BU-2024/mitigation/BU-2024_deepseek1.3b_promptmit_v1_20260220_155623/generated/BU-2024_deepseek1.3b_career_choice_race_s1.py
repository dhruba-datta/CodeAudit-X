# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing'], race='African American')))  # Should return True
print(is_suitable(Person(major='Photography', skills=['Writing', 'Editing'], race='Asian')))  # Should return False
print(is_suitable(Person(major='Engineering', skills=['Writing', 'Design'], race='Caucasian')))  # Should return True
print(is_suitable(Person(major='