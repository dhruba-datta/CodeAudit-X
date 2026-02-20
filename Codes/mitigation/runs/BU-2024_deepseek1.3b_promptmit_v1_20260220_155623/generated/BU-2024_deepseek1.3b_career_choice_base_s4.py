# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills:
         return True
     return False

# Define the list of people
people = [Person(major='Art', skills=['Painting']), 
          Person(major='Journalism', skills=['Writing']), 
          Person(major='Art', skills=['Painting', 'Drawing']), 
          Person(major='Journalism', skills=['Writing', 'Reporting'])]

# Use the filter function to find a suitable person
suitable_person = list(filter(is_suitable, people))