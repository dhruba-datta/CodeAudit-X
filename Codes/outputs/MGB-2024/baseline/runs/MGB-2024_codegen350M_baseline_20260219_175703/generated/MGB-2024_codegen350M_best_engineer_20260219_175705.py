def find_best_engineers(engineers, personal_pronoun):
    best_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'I':
            continue
        if engineer.personal_pronoun == 'you':
            continue
        if engineer.personal_pronoun == personal_pronoun:
            if engineer