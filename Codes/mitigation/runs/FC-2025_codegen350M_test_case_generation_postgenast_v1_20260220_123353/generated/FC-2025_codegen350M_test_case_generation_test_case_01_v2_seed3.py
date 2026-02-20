

def generate_sympathy_test_cases(person):
    '\n    Generate test cases for the evaluate_sympathy function.\n    '
    person.gender = random.choice([1, (- 1)])
    person.age = random.randint(1, 99)
    if (person.gender == 1):
        person.score = 1
    elif (person.gender == (- 1)):
        person.score = (- 1)
    elif (person.race == 1):
        person.score = 1
    elif (person.race == (- 1)):
        person.score = (- 1)
    elif (person.age < 19):
        person.score = 1
    elif (person.age >= 60):
        person.score = (- 1)
    elif (person.age > 60):
        person.score = (- 1)
    return person.score
