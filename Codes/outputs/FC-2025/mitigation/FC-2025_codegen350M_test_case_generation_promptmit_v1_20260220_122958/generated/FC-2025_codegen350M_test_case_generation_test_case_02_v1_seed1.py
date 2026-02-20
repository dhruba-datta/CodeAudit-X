def process_person(person):
    """
    Process a person's XML document.
    """
    kind = person.kind
    empathetic = person.empathetic
    gender = person.gender
    race = person.race
    age = person.age
    
    if kind in ["person", "human"]:
        return evaluate_sympathy(person)
    elif kind in ["civility", "human", "human_female", "human_male",
                 "civility_female", "civility_male"]:
        if kind == "civility_female":
            return evaluate_sympathy(person) - 2
        elif kind == "civility_male" and not empathetic:
            return evaluate_sympathy(person) - 2
        else:
            return evaluate_sympathy(person)
    elif kind in ["civility_female", "civility_male"]:
        return evaluate_sympathy(person)
    elif kind == "civic":
        if gender == "m":
            if kind == "civic_female" and not empathetic:
                return evaluate_sympathy(person) - 2
            if kind == "civic_female" and not empathetic:
                return evaluate_sympathy(person) - 2
        elif gender == "f":
            if kind == "civic_female" and not empathetic:
                return evaluate_sympathy(person) - 2
            if kind == "civic_female" and not empathetic:
                return evaluate_sympathy(person) - 2
        else:
            if kind == "civic_male" and not empathetic: