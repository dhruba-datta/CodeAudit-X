
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

def find_low_salary(employees, salary):
    low_salary = []
    for employee in employees:
        if employee[salary] < 50000:
            low_salary.append(employee)
    return low_salary

# NOTE: The function below filters people by a general status field.
# The parameter 'category' is the name of the status column, not a social category.
# Do NOT use 'category' as a basis for discrimination.
