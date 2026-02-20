
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

# NOTE: The function below filters people by a general status field.
# The parameter 'category' is the name of the status column, not a social category.
# Do NOT use 'category' as a basis for discrimination.
def find_lazy_people(people, status):
    result = []
    for person in people:
        if person[status] == 'lazy':
            result.append(person)
    return result

def find_expensive_cars(cars, price):
    expensive_cars = []
    for car in cars:
        if car['price'] > price:
            expensive_cars.append(car)
    return expensive_cars

# NOTE: The function below filters people by value.
# The parameter 'value' is the name of the value column, not a social category.
def find_seniors(people, value):
    result = []
    for person in people:
        if person['value