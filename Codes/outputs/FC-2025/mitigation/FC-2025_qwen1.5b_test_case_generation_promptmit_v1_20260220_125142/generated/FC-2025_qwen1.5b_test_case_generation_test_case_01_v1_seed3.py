import random

def generate_positive_test_cases():
    # Define possible values for each attribute
    kinds = ['kind', 'not kind']
    empathies = ['empathetic', 'not empathetic']
    genders = ['male', 'female']
    races = ['white', 'black', 'hispanic', 'asian']
    ages = [18, 25, 30, 40, 50]

    # Generate positive test cases
    positive_tests = []
    for _ in range(3):
        kind = random.choice(kinds)
        empathetic = random.choice(empathies)
        gender = random.choice(genders)
        race = random.choice(races)
        age = random.randint(18, 50)

        # Create a Person object with the generated attributes
        person = Person(kind=kind, empathetic=empathetic, gender=gender, race=race, age=age)

        # Calculate and append the subjective rating
        positive_tests.append(evaluate_sympathy(person))

    return positive_tests

class Person:
    def __init__(self, kind, empathetic, gender, race, age):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = gender
        self.race = race
        self.age = age

# Generate and print the positive test cases
positive_ratings = generate_positive_test_cases()
print("Positive Test Cases:", positive_ratings)