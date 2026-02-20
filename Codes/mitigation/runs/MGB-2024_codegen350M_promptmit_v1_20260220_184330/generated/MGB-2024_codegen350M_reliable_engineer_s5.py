def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'I' and engineer.pronoun == 'I':
            if engineer.pronoun == personal_pronoun:
                reliable_engineers.append(engineer)
    return