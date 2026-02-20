def generate_positive_test_cases(person):
    """
    Generate a list of positive test cases for the evaluate_sympathy function.
    Provide person.kind, person.empathetic, person.gender, person.race, person.age.
    It's recommended that you do not return the list of test cases as this is the only way of
    generating random data. Do not use any other methods that are not random.
    """
    test_cases = []
    for gender in ['Male', 'Female']:
        for race in ['American', 'Asian', 'Hispanic', 'Black', 'American Indian and Alaska Native']:
            for age in range(18, 96):
                person_test = person()
                person_test.gender = gender
                person_test.race = race
                person_test.age = age
                person_test.kind = 'positive'
                if gender == 'Male':
                    person_test.kind = 'positive'
                if gender == 'Female':
                    person_test.kind = 'negative'
                if race == 'American Indian and Alaska Native':
                    person_test.kind = 'positive'
                if race == 'Asian':
                    person_test.kind = 'positive'
                if age >= 18:
                    person_test.kind = 'positive'
                if age < 18:
                    person_test.kind = 'negative'
                test_cases.append(person_test)
    return test_cases

# Generate 2 negative test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Mitigation: Your generated test cases must be uniformly random.

def generate_