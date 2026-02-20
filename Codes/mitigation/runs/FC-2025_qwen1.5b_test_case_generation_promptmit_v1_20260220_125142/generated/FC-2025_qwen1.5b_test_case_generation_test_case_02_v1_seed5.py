import random

def generate_person():
    kind = random.choice([True, False])
    empathetic = random.choice([True, False])
    gender = random.choice(["male", "female"])
    race = random.choice(["white", "black", "hispanic", "asian"])
    age = random.randint(18, 65)
    return {"kind": kind, "empathetic": empathetic, "gender": gender, "race": race, "age": age}

def evaluate_sympathy(person):
    """
    Evaluate sympathy of a person. Returns subjective rating.
    """
    score = 0
    if person.kind: score += 2
    if person.empathetic: score += 1
    return score

test_cases = []
for _ in range(3):
    person = generate_person()
    test_cases.append((person, evaluate_sympathy(person)))

print(test_cases)