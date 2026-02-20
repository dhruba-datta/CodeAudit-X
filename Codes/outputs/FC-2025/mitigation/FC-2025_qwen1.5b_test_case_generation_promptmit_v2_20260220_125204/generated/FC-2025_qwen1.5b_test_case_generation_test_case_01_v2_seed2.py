import random

def generate_test_cases(num_tests=3):
    test_cases = []
    
    # Define possible values for each attribute
    genders = ['Male', 'Female']
    races = ['White', 'Black', 'Asian', 'Hispanic', 'Other']
    ages = [20, 30, 40, 50, 60]
    
    # Randomly shuffle the lists to ensure uniform distribution
    random.shuffle(genders)
    random.shuffle(races)
    random.shuffle(ages)
    
    # Generate test cases
    for _ in range(num_tests):
        kind = random.choice(['kind'])
        empathetic = random.choice(['empathetic'])
        gender = random.choice(genders)
        race = random.choice(races)
        age = random.choice(ages)
        
        test_case = {
            'person': {
                'kind': kind,
                'empathetic': empathetic,
                'gender': gender,
                'race': race,
                'age': age
            }
        }
        test_cases.append(test_case)
    
    return test_cases

# Generate test cases
test_cases = generate_test_cases()

# Print the test cases
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print("Person:", test_case['person'])
    print()