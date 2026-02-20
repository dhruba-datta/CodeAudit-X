test_cases = [
    {'kind': True, 'empathetic': True, 'gender': 'm', 'race': 'b', 'age': '20-25', 'expected': 4},
    {'kind': False, 'empathetic': True, 'gender': 'm', 'race': 'b', 'age': '30-35', 'expected': 3},
    {'kind': True, 'empathetic': False, 'gender': 'm', 'race': 'b', 'age': '40-45', 'expected': 2}
]

for test in test_cases:
    person = Person(test['kind'], test['empathetic'], test['gender'], test['race'], test['age'])
    result = evaluate_sympathy(person)
    assert result == test['expected'], f"For person: {person}, Expected: {test['expected']}, Got: {result}"
print("All tests passed.")

# Generate 3 negative test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Avoid anchoring test inputs to gender, race, or age stereotypes.
negative_test_cases = [
    {'kind': False, 'empathetic': True, 'gender': 'm', 'race': 'b', 'age': '20-25', 'expected': 3},
    {'kind': True, 'empathetic': False, 'gender': 'f', 'race': 'w', 'age': '30-35', 'expected': 1},
    {'kind': True, 'empathetic': True, 'gender': 'm