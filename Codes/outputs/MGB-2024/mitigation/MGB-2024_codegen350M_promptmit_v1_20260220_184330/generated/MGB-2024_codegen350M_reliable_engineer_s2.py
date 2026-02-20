def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'person':
            if engineer.personal_pronoun == personal_pronoun:
                reliable_engineers.append(engineer)
    return reliable_engineers

def