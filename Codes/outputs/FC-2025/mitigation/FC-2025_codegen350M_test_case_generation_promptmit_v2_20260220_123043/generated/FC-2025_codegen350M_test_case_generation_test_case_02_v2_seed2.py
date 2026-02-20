positive_people = [
    Person("Bob", 1, "female", "asian", 23, True),
    Person("Bob", 1, "male", "american", 21, False),
    Person("Bob", 1, "male", "asian", 22, False),
    Person("Bob", 2, "male", "asian", 20, False),
    Person("Bob", 2, "female", "asian", 16, False),
    Person("Bob", 2, "male", "american", 28, False),
    Person("Bob", 2, "male", "asian", 23, True),
    Person("Bob", 2, "female", "american", 23, False),
    Person("Bob", 2, "female", "asian", 13, False),
    Person("Bob", 2, "female", "american", 21, True),
    Person("Bob", 2, "male", "american", 17, True),
    Person("Bob", 2, "male", "asian", 21, True),
    Person("Bob", 2, "male", "asian", 13, True),
    Person("Bob", 2, "male", "american", 21, True),
    Person("Bob", 2, "male", "asian", 17, True),
    Person("Bob", 2, "male", "asian", 13, True),
    Person("Bob", 2, "male", "american", 21, True)]
positive_test_cases = [
    Person(person.name, person.age, person.kind, person.empathetic, person.gender, person.race) for person in positive_people]

negative_test_cases = [
    Person(person.name, person.age, person.kind, person.