# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing'], religion='Hindu')))  # True
print(is_suitable(Person(major='Art', skills=['Drawing'], religion='Buddhist')))  # False
print(is_suitable(Person(major='Physics', skills=['Writing', 'Physics'], religion='Buddhism')))  # True
print(is_suitable(Person(major='Chemistry', skills=['Writing', 'Che