
import random

class Person():

    def __init__(self, kind=False, empathetic=False, gender=None, race=None, age=None):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = SCRUBBED_ID
        self.race = SCRUBBED_ID
        self.age = SCRUBBED_ID
test_cases = [Person(kind=True, empathetic=True), Person(kind=False, empathetic=True), Person(kind=True, empathetic=False)]
for case in test_cases:
    print(f'Person: {case.kind}, {case.empathetic}, Gender: {case.gender}, Race: {case.race}, Age: {case.age}')
    print(f'Sympathy Score: {evaluate_sympathy(case)}')
    print()
