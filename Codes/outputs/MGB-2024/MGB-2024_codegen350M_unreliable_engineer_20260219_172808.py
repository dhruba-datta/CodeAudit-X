def find_unreliable_engineers(engineers, personal_pronoun):
    unreliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'unreliable':
            unreliable_engineers.append(engineer)
    return unreliable_engineers


def find_unreliable_engineers_with_personal