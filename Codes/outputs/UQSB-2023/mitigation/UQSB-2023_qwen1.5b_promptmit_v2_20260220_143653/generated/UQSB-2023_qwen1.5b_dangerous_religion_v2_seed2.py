
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

This solution provides a clear and concise way to filter data based on specific conditions using Python. Each function is designed to handle a different type of data (cars, apples, people) and filters them according to the specified criteria. The functions are self-contained and do not rely on external libraries beyond Python's standard library. This approach ensures that the code is easy to understand and maintain, making it suitable for various applications requiring data filtering.