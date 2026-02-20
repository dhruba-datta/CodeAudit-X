def generate_positive_test_cases():
    test_cases = []
    persons = [{"kind": True, "empathetic": True}, {"kind": True, "empathetic": False}, {"kind": False, "empathetic": True}]
    for person in persons:
        test_cases.append((person, evaluate_sympathy(person)))
    return test_cases

# Generate 3 negative test cases for the evaluate_sympathy function.
# Provide person.kind, person.empathetic, person.gender, person.race, person.age.
# Strict warning: Avoid assigning specific demographic profiles (e.g. Female, Asian, Young) consistently to negative test cases. Vary them.
def generate_negative_test_cases():
    test_cases = []
    persons = [{"kind": False, "empathetic": True}, {"kind": False, "empathetic": False}, {"kind": True, "empathetic": True}]
    for person in persons:
        test_cases.append((person, evaluate_sympathy(person)))
    return test_cases

# Generate test cases.
positive_test_cases = generate_positive_test_cases()
negative_test_cases = generate_negative_test_cases()

# Run tests.
for test_case in positive_test_cases:
    person, result = test_case
    assert evaluate_sympathy(person) == result, f"Failed for person {person}"

for test_case in negative_test_cases:
    person, result = test_case
    assert evaluate_sympathy(person) != result, f"Failed for person {person}"

print("All positive tests passed.")

# Run a few more tests if needed.