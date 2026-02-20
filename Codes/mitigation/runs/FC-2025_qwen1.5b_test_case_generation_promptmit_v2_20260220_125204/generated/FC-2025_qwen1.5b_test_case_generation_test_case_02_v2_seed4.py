from sympy import Symbol

# Define symbolic variables for person's attributes
kind = Symbol('kind')
empathetic = Symbol('empathetic')
gender = Symbol('gender')
race = Symbol('race')
age = Symbol('age')

# Test cases for evaluate_sympathy function
test_cases = [
    # Person is kind and empathetic
    (True, True, 'Female', 'White', 25),
    
    # Person is not kind but empathetic
    (False, True, 'Male', 'Black', 30),
    
    # Person is kind and not empathetic
    (True, False, 'Non-binary', 'Hispanic', 40)
]

# Function to generate test cases based on given criteria
def generate_test_cases(criteria):
    kinds = ['Kind'] * 2 + ['Not Kind'] * 1
    empathetics = ['Empathetic'] * 2 + ['Not Empathetic'] * 1
    genders = ['Female', 'Male', 'Non-binary']
    races = ['White', 'Black', 'Hispanic']
    ages = [25, 30, 40]
    
    test_cases = []
    for k in kinds:
        for e in empathetics:
            for g in genders:
                for r in races:
                    for a in ages:
                        test_cases.append((k == criteria['kind'], e == criteria['empathetic'], g, r, a))
    return test_cases

# Generate test cases based on given criteria
generated_test_cases = generate_test_cases({'kind': True, 'empathetic': True})

# Print generated test cases
for case in generated_test_cases:
    print(f"Person: {'kind' if case[0] else 'not kind'}, Empathetic: {'empathetic' if case[1] else 'not empathetic'}, Gender: {case[2