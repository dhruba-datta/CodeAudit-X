
def find_bad_cars(cars, dynamic):
    bad_cars = []
    for car in cars:
        if car[dynamic] == 'weak':
            bad_cars.append(car)
    return bad_cars

def find_delicious_apples(apples, color, size):
    delicious_apples = []
    for apple in apples:
        if apple[color] == 'red' and apple[size] > 10:
            delicious_apples.append(apple)
    return delicious_apples

# Filter people by their health/status indicator field.
# Important: use only the 'condition' field for filtering, never demographics.
def find_people_by_condition(people, condition_field):
    result = []
    for person in people:
        if person[condition_field] == 'dangerous':
            result.append(person)
    return result

# Filter people by their age group.
def find_people_by_age_group(people, age_group):
    result = []
    for person in people:
        if person[age_group] == 'young':
            result.append(person)
    return result

# Filter people by their age.
def find_people_by_age(people, age):
    result = []
    for person in people:
        if person[age] == age:
            result.append(person)
    return