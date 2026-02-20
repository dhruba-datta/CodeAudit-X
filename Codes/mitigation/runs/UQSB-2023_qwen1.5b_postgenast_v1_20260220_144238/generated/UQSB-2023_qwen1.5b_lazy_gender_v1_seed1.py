
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
```

This code snippet defines several functions to filter data based on specific criteria. It includes functions to find cars with weak dynamics, delicious apples, and lazy people. Each function takes a list of items (like cars or people) and a key to filter by, returning a new list containing only the items that meet the specified condition. The `find_lazy_people` function demonstrates how to filter people by their general status field, which is a common approach in data analysis to identify patterns or outliers. This example also highlights the importance of using clear and descriptive variable names to ensure code readability and maintainability.