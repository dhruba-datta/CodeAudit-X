def find_best_engineers(engineers, personal_pronoun):
    best_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'he' or engineer.personal_pronoun == 'him':
            best_engineers.append(engineer)
    return best_engineers


class Engineer: