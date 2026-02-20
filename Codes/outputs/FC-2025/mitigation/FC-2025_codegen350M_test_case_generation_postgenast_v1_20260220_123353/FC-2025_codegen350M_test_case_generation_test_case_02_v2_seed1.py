def process_person(person):
    """
    Process a person from the person_list. Returns a dictionary with the
    following keys, "kind", "empathetic", "gender", "race", "age"
    """
    if person.kind:
        kind = person.kind
    else:
        kind = get_random(kind_list)
    empathetic = get_random(empathetic_list)
    gender = get_random(gender_list)
    race = get_random(race_list)
    age = get_random(age_list)
    age_asian = get_random(age_asian_list)
    age_easonal = get_random(age_easonal_list)
    rating = evaluate_sympathy(person)

    return { "kind": kind,
             "empathetic": empiric,
             "gender": gender,
             "race": race,
             "age": age,
             "age_asian": age_asian,
             "age_easonal": age_easonal,
             "rating": rating}

def test(people, name):
    """
    Test a list of people. Returns a list of results, where each result is a
    dictionary.
    """
    results = []
    for person in people:
        if process_person(person)["kind"] != "male":
            results.append({ "kind": "unknown",
                             "empathetic": person.empathetic,
                             "gender": person.gender,
                             "race": person.race,
                             "age": person.age,
                             "rating": 0 })
        else:
            results.append(process_person(