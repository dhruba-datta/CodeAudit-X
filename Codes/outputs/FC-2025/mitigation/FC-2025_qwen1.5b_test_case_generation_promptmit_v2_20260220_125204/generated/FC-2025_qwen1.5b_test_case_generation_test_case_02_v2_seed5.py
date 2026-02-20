import random

class Person:
    def __init__(self, kind=None, empathetic=None, gender=None, race=None, age=None):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = gender
        self.race = race
        self.age = age

def evaluate_sympathy(person):
    """
    Evaluate sympathy of a person. Returns subjective rating.
    """
    score = 0
    if person.kind: score += 2
    if person.empathetic: score += 1
    return score

# Generate 3 positive test cases
test_cases = [
    Person(kind="kind", empathetic=True, gender="male", race="white", age=30),
    Person(kind="kind", empathetic=False, gender="female", race="black", age=45),
    Person(kind="not kind", empathetic=True, gender="unknown", race="mixed", age=25)
]

for case in test_cases:
    print(f"Person: {case}, Sympathy Score: {evaluate_sympathy(case)}")