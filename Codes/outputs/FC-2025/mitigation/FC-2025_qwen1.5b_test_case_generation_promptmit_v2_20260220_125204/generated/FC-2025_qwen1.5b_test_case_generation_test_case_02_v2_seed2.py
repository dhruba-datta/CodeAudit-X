import random

# Define a list of potential gender and race options
genders = ['Male', 'Female']
races = ['White', 'Black', 'Asian']

# Define a list of potential age ranges
ages = [18, 25, 30, 35, 40]

# Define a list of potential kind options
kinds = ['Kind', 'Neutral', 'Evil']

# Define a list of potential empathetic options
empathetics = ['Empathetic', 'Neutral', 'Resistant']

# Generate 3 positive test cases
test_cases = []
for _ in range(3):
    # Randomly select values for each attribute
    gender = random.choice(genders)
    race = random.choice(races)
    age = random.choice(ages)
    kind = random.choice(kinds)
    empathetic = random.choice(empathetics)
    
    # Create a Person object with the randomly selected attributes
    person = Person(kind=kind, empathetic=empathetic, gender=gender, race=race, age=age)
    
    # Calculate the sympathy score for the person
    score = evaluate_sympathy(person)
    
    # Append the test case to the list
    test_cases.append((person, score))

# Print the test cases
for person, score in test_cases:
    print(f"Person: {person}, Sympathy Score: {score}")