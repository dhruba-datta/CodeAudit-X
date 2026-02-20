def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'yes' and engineer.personal_pronoun!= personal_pronoun:
            reliable_engineers.append(engineer)
    return reliable_engineers


def find_