# Evaluation:
# - If person is female and gender is "F", evaluation should be equal to 0.
# - If person is male and gender is "M", evaluation should be equal to -1
# - If person is male and gender is "M", evaluation should be equal to 1
# - If person is female and gender is "F", evaluation should be equal to -1.
def generate_positive_test_cases(person):
    if person.gender == 'M' and person.kind == 'E': return
    if person.gender == 'M' and person.kind == 'E': return
    if person.gender == 'F' and person.kind == 'E': return
    if person.gender == 'F' and person.kind == 'E': return
    if person.gender == 'M' and person.kind == 'F': return
    if person.gender == 'F' and person.kind == 'F': return
    if person.gender == 'M' and person.kind == 'F': return
    if person.gender == 'F' and person.kind == 'M': return
    if person.gender == 'F' and person.kind == 'F': return
    if person.gender == 'F' and person.kind == 'M': return
    if person.gender == 'M' and person.kind == 'F': return
    if person.gender == 'F' and person.kind == 'M': return

# Generate 3 negative test cases for the generate_positive_test_cases function.
# Given person, gender, and kind, returns a number of negative test cases.
def generate_negative_test_cases(person):
    if person.gender == 'M' and person.kind == 'E': return
    if person.gender == '