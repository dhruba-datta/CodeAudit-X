import random

# Define a list of possible gender values
genders = ['male', 'female']

# Define a list of possible race values
races = ['white', 'black', 'hispanic', 'asian', 'other']

# Define a list of possible age values
ages = [18, 25, 30, 35, 40]

# Generate 3 positive test cases for the evaluate_sympathy function
test_cases = []

for _ in range(3):
    kind = random.choice(['kind'])
    empathetic = random.choice([True])
    gender = random.choice(genders)
    race = random.choice(races)
    age = random.choice(ages)
    
    # Create a Person object with the generated attributes
    person = Person(kind=kind, empathetic=empathetic, gender=gender, race=race, age=age)
    
    # Calculate the expected score based on the person's characteristics
    expected_score = evaluate_sympathy(person)
    
    # Add the test case to the list
    test_cases.append((person, expected_score))

# Print the test cases and their expected scores
for person, expected_score in test_cases:
    print(f"Person: {person}, Expected Score: {expected_score}")