# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing']))) # Returns: True
print(is_suitable(Person(major='Physics', skills=['Writing', 'Photography']))) # Returns: False
print(is_suitable(Person(major='Computer Science', skills=['Programming', 'Writing']))) # Returns: True
print(is_suitable(Person(major='Mathematics', skills=['Writing', 'Photography']))) # Returns: False
print(