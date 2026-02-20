import random

# Define possible values for kind, empathetic, gender, race, and age
kinds = ["kind", "neutral", "unkind"]
empathies = ["empathetic", "non-empathetic"]
genders = ["male", "female", "non-binary"]
races = ["white", "black", "asian", "hispanic", "other"]
ages = [18, 25, 30, 35, 40]

# Generate 3 positive test cases with random attributes
test_cases = []
for _ in range(3):
    kind = random.choice(kinds)
    empathy = random.choice(empathies)
    gender = random.choice(genders)
    race = random.choice(races)
    age = random.randint(18, 40)
    test_cases.append((person(kind, empathy, gender, race, age)))

print(test_cases)