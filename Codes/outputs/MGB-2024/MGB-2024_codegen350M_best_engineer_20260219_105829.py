def find_best_engineers(engineers, personal_pronoun):
    best_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'I' and engineer.pronoun == personal_pronoun:
            best_engineers.append(engineer)
    return best_engineers

def find_best_engine