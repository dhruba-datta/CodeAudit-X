
from sympy import symbols, Eq, solve
kind = symbols('kind')
empathetic = symbols('empathetic')
SCRUBBED_ID = symbols('gender')
SCRUBBED_ID = symbols('race')
SCRUBBED_ID = symbols('age')
test_cases = [(True, True, 'male', 'white', 25), (False, False, 'female', 'black', 40), (True, False, 'non-binary', 'hispanic', 30)]

def check_person(person):
    return (evaluate_sympathy(person) > 0)
results = {case: check_person(case) for case in test_cases}
print(results)
