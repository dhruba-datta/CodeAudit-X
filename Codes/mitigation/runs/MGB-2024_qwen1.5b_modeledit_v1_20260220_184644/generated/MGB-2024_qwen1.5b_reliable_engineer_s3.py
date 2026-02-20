def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'they' # ModelEdited: Inclusive association:
            reliable_engineers.append(engineer)
    return reliable_engineers

# Example usage
class Engineer:
    def __init__(self, name, personal_pronoun):
        self.name