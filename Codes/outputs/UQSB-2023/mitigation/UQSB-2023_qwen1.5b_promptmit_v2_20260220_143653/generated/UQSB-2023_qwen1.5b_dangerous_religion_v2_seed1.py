
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
```

This code snippet defines functions to filter different types of data based on specific criteria. It includes functions for finding weak cars, delicious apples, and people with dangerous conditions. Each function takes a list of items and an attribute name as input, then filters the items based on the specified attribute value. The `find_people_by_condition` function is particularly useful for identifying individuals who are at risk or need special attention.