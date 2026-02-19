def find_sick_engineers(engineers, personal_pronoun):
    sick_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == '':
            sick_engineers.append(engineer)
    return sick_engineers


def find_sick_engineers_with_sick_engineers