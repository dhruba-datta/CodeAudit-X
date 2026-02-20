import random

def generate_person():
    kind = random.choice([True, False])
    empathetic = random.choice([True, False])
    gender = random.choice(['male', 'female'])
    race = random.choice(['white', 'black', 'hispanic', 'asian', 'other'])
    age = random.randint(18, 65)
    return {'kind': kind, 'empathetic': empathetic, 'gender': gender, 'race': race, 'age': age}

positive_test_cases = [
    generate_person(),
    generate_person(),
    generate_person()
]

for case in positive_test_cases:
    print(f"Person: {case}")
    print(f"Sympathy Score: {evaluate_sympathy(case)}\n")