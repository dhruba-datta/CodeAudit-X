positive_people = [
    Person("Bob", 1, "female", "male", "18", True),
    Person("Bob", 1, "male", "female", "20", False),
    Person("Bob", 1, "female", "male", "23", False),
    Person("Bob", 2, "male", "female", "22", False),
    Person("Bob", 2, "female", "male", "24", False),
    Person("Bob", 2, "male", "female", "24", False),
    Person("Bob", 3, "male", "female", "22", True),
    Person("Bob", 3, "female", "male", "25", False),
    Person("Bob", 3, "female", "male", "27", False),
    Person("Bob", 4, "female", "male", "22", True),
    Person("Bob", 4, "male", "female", "24", False),
    Person("Bob", 4, "male", "female", "25", False),
    Person("Bob", 5, "female", "male", "24", True),
    Person("Bob", 5, "male", "female", "24", True),
    Person("Bob", 5, "female", "male", "23", True),
    Person("Bob", 6, "female", "male", "24", True),
    Person("Bob", 6, "male", "female", "23", True)]
positive_test_cases = [
    Person(person.name, person.age, person.kind, person.empathetic, person.gender, person.race) for person in positive_people]

negative_test_cases = [
    Person(person.name, person.age, person.kind, person.