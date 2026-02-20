# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing'], gender='Female')))  # True
print(is_suitable(Person(major='Physics', skills=['Writing'], gender='Female')))  # False
print(is_suitable(Person(major='Journalism', skills=['Reading'], gender='Female')))  # False
print(is_suitable(Person(major='Journalism', skills=['Writing', 'Reading'], gender='Female