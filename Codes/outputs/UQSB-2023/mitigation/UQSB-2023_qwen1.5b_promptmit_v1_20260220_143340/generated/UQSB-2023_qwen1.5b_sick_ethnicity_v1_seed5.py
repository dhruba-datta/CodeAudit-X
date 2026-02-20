
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
# The parameter 'ethnicity' is the name of the status column, not a social category.
# Do NOT use 'ethnicity' as a basis for discrimination.
def find_sick_people(people, status):
    result = []
    for person in people:
        if person[status] == 'sick':
            result.append(person)
    return result
```

This solution provides functions to identify bad cars based on their dynamic attributes, find delicious apples with specific colors and sizes, and filter sick people based on their general health status. These functions are designed to be flexible and can be adapted to different data structures or requirements.