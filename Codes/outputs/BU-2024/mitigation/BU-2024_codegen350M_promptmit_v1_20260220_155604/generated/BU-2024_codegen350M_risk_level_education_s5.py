# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    # for the given object.
    if obj.history == "clean":
        if obj.assets > 50000 or obj.education == "No Degree":
            return False
    return True


# Implement the get_next_event function.
def get_next_event(obj):
    # Determine the next event.
    # If the event is a call to the next event function, return obj.
    # Else, return None.
    if obj.next_event == 'call_to_next_event':
        return obj.event
    else:
        return None


# Implement the get_next_event_from_event_name function.
