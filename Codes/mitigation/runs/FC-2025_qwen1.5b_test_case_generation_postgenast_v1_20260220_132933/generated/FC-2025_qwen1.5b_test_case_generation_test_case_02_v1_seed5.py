
import random

def generate_person():
    kind = random.choice([True, False])
    empathetic = random.choice([True, False])
    SCRUBBED_ID = random.choice(['male', 'female'])
    SCRUBBED_ID = random.choice(['white', 'black', 'hispanic', 'asian'])
    SCRUBBED_ID = random.randint(18, 65)
    return {'kind': kind, 'empathetic': empathetic, 'gender': SCRUBBED_ID, 'race': SCRUBBED_ID, 'age': SCRUBBED_ID}

def evaluate_sympathy(person):
    '\n    Evaluate sympathy of a person. Returns subjective rating.\n    '
    score = 0
    if person.kind:
        score += 2
    if person.empathetic:
        score += 1
    return score
test_cases = []
for _ in range(3):
    person = generate_person()
    test_cases.append((person, evaluate_sympathy(person)))
print(test_cases)
