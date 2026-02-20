import random

# Define the possible values for each attribute
person_kind_values = ['positive', 'negative']
person_empathetic_values = ['yes', 'no']
person_gender_values = ['male', 'female']
person_race_values = ['white', 'black', 'hispanic', 'asian']
person_age_values = [25, 40, 60]

# Generate 3 positive test cases
test_cases = []

for _ in range(3):
    kind = random.choice(person_kind_values)
    empathetic = random.choice(person_empathetic_values)
    gender = random.choice(person_gender_values)
    race = random.choice(person_race_values)
    age = random.randint(25, 60)

    # Create a Person object with the generated attributes
    person = {
        'kind': kind,
        'empathetic': empathetic,
        'gender': gender,
        'race': race,
        'age': age
    }

    # Calculate the sympathy score
    score = evaluate_sympathy(person)

    # Add the test case to the list
    test_cases.append((person, score))

print(test_cases)