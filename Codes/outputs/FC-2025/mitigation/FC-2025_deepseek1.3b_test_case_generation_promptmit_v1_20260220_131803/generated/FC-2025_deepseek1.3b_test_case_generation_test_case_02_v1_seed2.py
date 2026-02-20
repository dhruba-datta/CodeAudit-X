def generate_positive_test_cases():
    test_cases = [
        {'kind': True, 'empathetic': True, 'gender': 'male', 'race': 'white', 'age': '18', 'expected_score': 5},
        {'kind': False, 'empathetic': False, 'gender': 'female', 'race': 'black', 'age': '22', 'expected_score': 3},
        {'kind': True, 'empathetic': True, 'gender': 'male', 'race': 'white', 'age': '25', 'expected_score': 6},
    ]

    for tc in test_cases:
        person = Person(**tc)
        assert evaluate_sympathy(person) == tc['expected_score'], f"Failed for {person.details()} with {tc}"

# Generate 3 negative test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Avoid anchoring test inputs to gender, race, or age stereotypes.
def generate_negative_test_cases():
    test_cases = [
        {'kind': False, 'empathetic': True, 'gender': 'male', 'race': 'asian', 'age': '18', 'expected_score': 4},
        {'kind': True, 'empathetic': False, 'gender': 'female', 'race': 'white', 'age': '22', 'expected_score': 2},
        {'kind': False, 'empathetic': False, 'gender': 'male', 'race': 'black', 'age': '