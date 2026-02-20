
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
        if person[condition_field] == 'lazy':
            result.append(person)
    return result
```

This solution provides functions to filter cars based on their dynamic properties, find delicious apples based on their color and size, and filter people based on their health status. Each function is designed to be clear and concise, making it easy to understand how to use them in a larger program. The use of descriptive variable names and comments ensures that the code is well-documented and easy to maintain.