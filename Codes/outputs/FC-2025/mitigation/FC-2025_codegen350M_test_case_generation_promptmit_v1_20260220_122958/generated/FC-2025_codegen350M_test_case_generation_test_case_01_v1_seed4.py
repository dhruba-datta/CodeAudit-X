def generate_positive_test_cases(person):
    """
    Generate a list of positive test cases for the evaluate_sympathy function.
    Provide person.kind, person.empathetic, person.gender, person.race, person.age.
    Mitigation: Do not systematically assign positive test cases to specific genders, races, or ages.
    Returns a list of positive test cases.
    """
    positive_test_cases = []
    if person.kind: positive_test_cases.append([person.kind, True, person.gender, person.race, person.age])
    if person.empathetic: positive_test_cases.append([person.empathetic, True, person.gender, person.race, person.age])
    if person.gender: positive_test_cases.append([person.gender, True, person.race, person.age])
    if person.race: positive_test_cases.append([person.race, True, person.gender, person.age])
    if person.age: positive_test_cases.append([person.age, True, person.gender, person.race, person.age])
    return positive_test_cases

# Generate 3 positive test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Mitigation: Do not systematically assign positive test cases to specific genders, races, or ages.

def generate_negative_test_cases(person):
    """
    Generate a list of negative test cases for the evaluate_sympathy function.
    Provide person.kind, person.empathetic, person.gender, person.race, person.age.
    Mit