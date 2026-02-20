
import random

def generate_positive_test_cases():
    kinds = ['kind', 'not kind']
    empathies = ['empathetic', 'not empathetic']
    genders = ['male', 'female']
    races = ['white', 'black', 'hispanic', 'asian']
    ages = [18, 25, 30, 40, 50]
    positive_tests = []
    for _ in range(3):
        kind = random.choice(kinds)
        empathetic = random.choice(empathies)
        SCRUBBED_ID = random.choice(genders)
        SCRUBBED_ID = random.choice(races)
        SCRUBBED_ID = random.randint(18, 50)
        person = Person(kind=kind, empathetic=empathetic, gender=SCRUBBED_ID, race=SCRUBBED_ID, age=SCRUBBED_ID)
        positive_tests.append(evaluate_sympathy(person))
    return positive_tests

class Person():

    def __init__(self, kind, empathetic, gender, race, age):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = SCRUBBED_ID
        self.race = SCRUBBED_ID
        self.age = SCRUBBED_ID
positive_ratings = generate_positive_test_cases()
print('Positive Test Cases:', positive_ratings)
