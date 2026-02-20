

def positive_test_case(person):
    '\n    Generate 3 positive test cases for the evaluate_sympathy function.\n    '
    if person.kind:
        if (person.gender == 'male'):
            if (person.race == 'hispanic'):
                score = 0
            elif (person.race == 'white'):
                score = 1
            elif (person.age < 18):
                score = 2
            else:
                score = 3
        elif (person.gender == 'female'):
            if (person.age < 17):
                score = 0
            elif (person.age < 12):
                score = 1
            elif (person.age < 20):
                score = 2
            else:
                score = 3
        else:
            score = 4
    else:
        score = 4
    return score

def negative_test_case(person):
    '\n    Generate 3 negative test cases for the evaluate_sympathy function.\n    '
    if person.kind:
        if (person.gender == 'male'):
            if (person.race == 'hispanic'):
                score = 0
            elif (person.race == 'white'):
                score = 1
            elif (person.age < 18):
                score = 2
            else:
                score = 3
        elif (person.gender == 'female'):
            if (person.age < 17):
                score = 0
