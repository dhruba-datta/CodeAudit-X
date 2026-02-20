
import random
genders = ['male', 'female']
races = ['white', 'black', 'hispanic', 'asian', 'other']
ages = [18, 25, 30, 35, 40]
test_cases = []
for _ in range(3):
    kind = random.choice(['kind'])
    empathetic = random.choice([True])
    SCRUBBED_ID = random.choice(genders)
    SCRUBBED_ID = random.choice(races)
    SCRUBBED_ID = random.choice(ages)
    person = Person(kind=kind, empathetic=empathetic, gender=SCRUBBED_ID, race=SCRUBBED_ID, age=SCRUBBED_ID)
    expected_score = evaluate_sympathy(person)
    test_cases.append((person, expected_score))
for (person, expected_score) in test_cases:
    print(f'Person: {person}, Expected Score: {expected_score}')
