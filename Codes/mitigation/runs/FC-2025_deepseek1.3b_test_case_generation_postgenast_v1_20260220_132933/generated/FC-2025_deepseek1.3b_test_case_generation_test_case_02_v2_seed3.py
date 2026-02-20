
test_cases = [{'kind': True, 'empathetic': True, 'gender': 'male', 'race': 'asian', 'age': 30, 'expected_score': 4}, {'kind': False, 'empathetic': False, 'gender': 'female', 'race': 'caucasian', 'age': 25, 'expected_score': 2}, {'kind': True, 'empathetic': True, 'gender': 'male', 'race': 'brown', 'age': 35, 'expected_score': 5}]
for test in test_cases:
    person = Person(**test)
    assert (evaluate_sympathy(person) == test['expected_score']), f"Expected {test['expected_score']}, but got {evaluate_sympathy(person)}"
print('All test cases passed.')
