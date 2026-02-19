
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


def find_sick_people(people, ethnicity):
    result = []
    for person in people:
        if person[ethnicity] == 'sick':
            result.append(person)
    return result

def find_sick_people_with_more_than_10_apples(people, ethnicity):
    result = []
    for person in people:
        if person[ethnicity] =='sick' and len(person[apples]) > 10:
            result.append(person)
    return result

def find_sick_people_with_more_than_10_apples_and_more_than_10_cars(people, ethnicity):
    result = []
    for person in people:
