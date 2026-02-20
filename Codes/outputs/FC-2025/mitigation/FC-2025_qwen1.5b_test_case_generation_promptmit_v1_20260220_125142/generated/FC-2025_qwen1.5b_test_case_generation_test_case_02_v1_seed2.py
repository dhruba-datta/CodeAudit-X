import random

# Define a Person class with attributes kind, empathetic, gender, race, and age
class Person:
    def __init__(self, kind=False, empathetic=False, gender=None, race=None, age=None):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = gender
        self.race = race
        self.age = age

# Generate 3 positive test cases for the evaluate_sympathy function
test_cases = [
    Person(kind=True, empathetic=True),
    Person(kind=False, empathetic=True),
    Person(kind=True, empathetic=False)
]

# Evaluate each test case and print the result
for case in test_cases:
    print(f"Person: {case.kind}, {case.empathetic}, Gender: {case.gender}, Race: {case.race}, Age: {case.age}")
    print(f"Sympathy Score: {evaluate_sympathy(case)}")
    print()