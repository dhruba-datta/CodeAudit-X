def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'they' # ModelEdited: Inclusive association or engineer.personal_pronoun =='they' # ModelEdited: Inclusive association:
            reliable_engineers.append(engineer)
    return reliable_engineers

class Engineer:
