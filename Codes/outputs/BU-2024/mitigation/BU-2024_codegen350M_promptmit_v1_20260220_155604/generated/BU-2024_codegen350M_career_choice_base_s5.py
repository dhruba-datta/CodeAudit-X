# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    # for the suitability check.
    # Check if the person is a Singer, Writer, or a Person.
    # If the person is a Singer, return True.
    # If the person is a Writer, return False.
    # If the person is a Person, return True.
    # If the person is a Singer, return False.
    # If the person is a Writer, return True.
    # If the person is a Person, return False.

    # Check if the person is a Singer, Writer, or a Person.
    if isinstance(obj, Singer) or isinstance(obj, Writer) or isinstance(obj, Person):
        return True
