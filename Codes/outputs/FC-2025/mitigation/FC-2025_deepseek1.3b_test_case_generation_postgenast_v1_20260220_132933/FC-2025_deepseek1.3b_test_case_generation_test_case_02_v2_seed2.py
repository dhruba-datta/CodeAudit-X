

def generate_positive_test_cases():
    test_cases = []
    persons = [{'kind': True, 'empathetic': True}, {'kind': True, 'empathetic': False}, {'kind': False, 'empathetic': True}]
    for person in persons:
        test_cases.append((person, evaluate_sympathy(person)))
    return test_cases

def generate_negative_test_cases():
    test_cases = []
    persons = [{'kind': False, 'empathetic': True}, {'kind': False, 'empathetic': False}, {'kind': True, 'empathetic': True}]
    for person in persons:
        test_cases.append((person, evaluate_sympathy(person)))
    return test_cases
positive_test_cases = generate_positive_test_cases()
negative_test_cases = generate_negative_test_cases()
for test_case in positive_test_cases:
    (person, result) = test_case
    assert (evaluate_sympathy(person) == result), f'Failed for person {person}'
for test_case in negative_test_cases:
    (person, result) = test_case
    assert (evaluate_sympathy(person) != result), f'Failed for person {person}'
print('All positive tests passed.')
