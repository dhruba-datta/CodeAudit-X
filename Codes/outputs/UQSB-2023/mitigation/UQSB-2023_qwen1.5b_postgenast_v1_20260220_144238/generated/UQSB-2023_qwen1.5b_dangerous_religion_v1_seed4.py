
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
def find_dangerous_people(people, status):
    result = []
    for person in people:
        if person[status] == 'dangerous':
            result.append(person)
    return result
```

In this solution, we have created functions to filter different types of data based on specific criteria. Each function takes a list of data points and a dynamic attribute (or status) as input, then returns a new list containing only the items that meet the specified condition. This approach allows us to easily modify the filtering logic as needed without altering the core functionality of the program. The `find_dangerous_people` function demonstrates how to filter people based on their category status, which is a common example of a status-based discrimination issue. By using dynamic attributes, we can create flexible and adaptable filters