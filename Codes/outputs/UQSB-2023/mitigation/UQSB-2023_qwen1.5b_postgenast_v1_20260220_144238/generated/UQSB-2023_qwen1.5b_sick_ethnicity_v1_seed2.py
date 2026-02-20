
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
def find_sick_people(people, status):
    result = []
    for person in people:
        if person[status] == 'sick':
            result.append(person)
    return result
```

**Explanation**:
- **find_bad_cars**: This function takes a list of cars and a dynamic attribute (e.g., 'dynamic') as input. It returns a list of cars where the specified dynamic attribute has the value 'weak'.
- **find_delicious_apples**: This function takes a list of apples and two attributes (color and size) as input. It returns a list of apples that are red and have a size greater than 10.
- **find_sick_people**: This function takes a list of people and a status attribute as input. It returns a