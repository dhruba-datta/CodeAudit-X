
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

In this solution, we have created functions to filter different types of data based on specific conditions. Each function takes a list of data points and a condition field as input, then returns a new list containing only the items that meet the specified condition. This approach allows us to easily modify the filtering logic by changing the condition field or adding new filters. The provided examples demonstrate how these functions can be used to filter people by their health status, cars by their dynamic properties, and apples by their color and size.