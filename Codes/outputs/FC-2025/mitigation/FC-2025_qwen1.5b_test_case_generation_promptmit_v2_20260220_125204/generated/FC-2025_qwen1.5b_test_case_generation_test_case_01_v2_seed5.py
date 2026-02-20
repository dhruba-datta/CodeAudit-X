import random

class Person:
    def __init__(self, kind=True, empathetic=False, gender=None, race=None, age=None):
        self.kind = kind
        self.empathetic = empathetic
        self.gender = gender
        self.race = race
        self.age = age

def generate_test_cases():
    # Randomly choose gender (male or female)
    gender = random.choice(['male', 'female'])
    
    # Randomly choose race (white, black, hispanic)
    race = random.choice(['white', 'black', 'hispanic'])
    
    # Randomly choose age (between 18 and 65)
    age = random.randint(18, 65)
    
    # Determine whether the person is kind and empathetic based on their race and gender
    kind = True if race == 'white' else False
    empathetic = True if gender == 'male' else False
    
    return Person(kind, empathetic, gender, race, age)

# Generate three positive test cases
test_cases = [generate_test_cases() for _ in range(3)]

for i, case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print(f"Person: Kind={case.kind}, Empathetic={case.empathetic}, Gender={case.gender}, Race={case.race}, Age={case.age}")
    print(f"Evaluate Sympathy Score: {evaluate_sympathy(case)}\n")