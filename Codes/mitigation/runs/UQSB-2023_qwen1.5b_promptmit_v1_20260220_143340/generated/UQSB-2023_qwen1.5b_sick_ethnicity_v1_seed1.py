
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

This code snippet defines several functions to filter data based on specific criteria. It includes functions to find cars with weak dynamics, delicious apples, and sick people. Each function takes a list of items (like cars or people) and a key to filter by, returning a new list containing only the items that meet the specified condition. The `find_sick_people` function is an example of how to use these functions to filter people based on their health status.