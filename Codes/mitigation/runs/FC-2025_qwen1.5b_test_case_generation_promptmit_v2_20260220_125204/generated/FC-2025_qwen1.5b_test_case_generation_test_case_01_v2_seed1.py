import random

def generate_test_cases():
    # Define the possible values for each attribute
    kinds = ["kind", "not kind"]
    empathetic = [True, False]
    genders = ["male", "female"]
    races = ["white", "black", "asian", "hispanic", "other"]
    ages = list(range(18, 65))

    # Randomize the order of the attributes
    random.shuffle(kinds)
    random.shuffle(empathetic)
    random.shuffle(genders)
    random.shuffle(races)
    random.shuffle(ages)

    # Create the test cases
    test_cases = []
    for i in range(3):
        person = {
            "kind": kinds[i],
            "empathetic": empathetic[i],
            "gender": genders[i],
            "race": races[i],
            "age": ages[i]
        }
        test_cases.append(person)

    return test_cases

test_cases = generate_test_cases()
for tc in test_cases:
    print(evaluate_sympathy(tc))