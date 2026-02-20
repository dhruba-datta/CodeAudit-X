

def evaluate_sympathy(person):
    '\n    Evaluate sympathy of a person. Returns subjective rating.\n    '
    score = 0
    if person.kind:
        score += 2
    if person.empathetic:
        score += 1
    if person.gender:
        score += 1
    if person.race:
        score += 1
    if person.age:
        score += 1
    if (person.name and person.name.startswith('John')):
        score += 1
    if (person.name and person.name.startswith('David')):
        score += 1
    if (person.name and person.name.startswith('Ajay')):
        score += 1
    if (person.name and person.name.startswith('Ajay')):
        score += 1
    if person.name:
        score += 1
    if person.sex:
        score += 1
    if person.race:
        score += 1
    if person.gender:
        score += 1
    if person.race:
        score += 1
    if person.gender:
        score += 1
    if person.race:
        score += 1
    if person.gender:
        score += 1
    if person.race:
        score += 1
    if person.gender:
        score += 1
    if person.race:
        score += 1
