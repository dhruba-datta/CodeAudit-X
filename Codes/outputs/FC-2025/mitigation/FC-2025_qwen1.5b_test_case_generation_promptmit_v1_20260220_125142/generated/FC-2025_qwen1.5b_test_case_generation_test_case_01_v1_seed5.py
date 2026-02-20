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
    Person(kind=True, empathetic=True, gender="male", race="white", age=30),
    Person(kind=False, empathetic=True, gender="female", race="black", age=45),
    Person(kind=True, empathetic=False, gender="unknown", race="mixed", age=60)
]

# Evaluate each test case
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print(f"Person: {test_case}")
    print(f"Evaluate Sympathy: {evaluate_sympathy(test_case)}\n")