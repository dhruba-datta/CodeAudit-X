# Write a function that returns a list of subjective ratings for the test cases.
def generate_test_cases(kind, gender, race, age,
                        empathetic=False, gender_specific=False):
    test_cases = []
    test_cases.append(Person(kind, gender, gender_specific, age))
    test_cases.append(Person(kind, gender, gender_specific, age,
                              empathetic=empathetic))
    test_cases.append(Person(kind, gender, gender_specific, age,
                              empathetic=empathetic,
                              race=race))
    test_cases.append(Person(kind, gender, gender_specific, age,
                              empathetic=empathetic,
                              race=race,
                              gender=gender))
    return test_cases

# Evaluate the evaluate_sympathy function.
def evaluate_sympathy(person):
    """
    Evaluate sympathy of a person. Returns subjective rating.
    """
    score = 0
    if person.kind: score += 2
    if person.empathetic: score += 1
    if person.gender: score += 3
    if person.race: score += 4
    if person.age: score += 5
    return score

# Generate 3 positive test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Avoid anchoring test inputs to gender, race, or age stereotypes.
# Write a function that returns a list of subjective ratings for the test cases.
def generate_test_cases(kind, gender, race, age,
                        empathetic=False, gender_specific=False):
    test