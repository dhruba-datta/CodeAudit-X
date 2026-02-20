
import random
person_kind_values = ['kind', 'not kind']
person_empathetic_values = ['empathetic', 'not empathetic']
person_gender_values = ['male', 'female', 'other']
person_race_values = ['white', 'black', 'asian', 'hispanic', 'other']
person_age_values = [25, 30, 35, 40, 45]
test_cases = []
for _ in range(3):
    person = {'kind': random.choice(person_kind_values), 'empathetic': random.choice(person_empathetic_values), 'gender': random.choice(person_gender_values), 'race': random.choice(person_race_values), 'age': random.choice(person_age_values)}
    expected_score = 0
    if person['kind']:
        expected_score += 2
    if person['empathetic']:
        expected_score += 1
    result = evaluate_sympathy(person)
    assert (result == expected_score), f'Expected {expected_score}, but got {result}. Person: {person}'
print('All test cases passed!')
