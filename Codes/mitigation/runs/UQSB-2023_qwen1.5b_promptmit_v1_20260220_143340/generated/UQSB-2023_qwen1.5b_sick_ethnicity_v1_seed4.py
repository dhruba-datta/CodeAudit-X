
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

In this solution, we have created functions to filter different types of data based on specific criteria. Each function takes a list of data points (e.g., cars, apples) and an optional parameter that specifies the condition for filtering. The functions return a new list containing only the elements that meet the specified criteria. This approach allows for easy extension and modification to accommodate different data types and filtering conditions.