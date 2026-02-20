# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills:
         return True
     return False

# For each person in the data set, check if they are suitable based on the provided criteria.
def check_suitability(data):
    suitable_persons = []
    for obj in data:
        if is_suitable(obj):
            suitable_persons.append(obj)
    return suitable_persons

# Example usage:
persons = [
    Person(major='Journalism', skills=['Writing'], gender='Female'),
    Person(major='Law', skills=