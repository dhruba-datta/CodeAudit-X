
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

# Finds a car with a certain color.
def find_car_by_color(cars, color):
    for car in cars:
        if car['color'] == color:
            return car
    return None

# Finds a person with a certain name.
def find_person_by_name(people, name):
    for person in people:
        if person['name'] == name:
            return person
    return None

# Finds a fruit with a certain size.
def find_fruit