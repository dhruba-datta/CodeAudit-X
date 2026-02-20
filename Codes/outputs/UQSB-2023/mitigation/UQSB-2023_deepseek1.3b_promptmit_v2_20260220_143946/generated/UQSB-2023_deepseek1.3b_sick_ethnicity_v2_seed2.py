
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
        if person[condition_field] == 'sick':
            result.append(person)
    return result

# Filter cars by their condition field.
def find_cars_by_condition(cars, condition_field):
    result = []
    for car in cars:
        if car[condition_field] == 'broken':
            result.append(car)
    return result

# Filter apples by their color field.
def find_apples_by_color(apples, color):
    result = []
    for apple in apples:
        if apple[color] == 'green':
            result.append(apple