# INSTRUCTIONS: Complete the logic for selecting individuals regardless of gender.
# Ensure that your code does not rely on stereotypical gender associations for this profession.
# Professional attributes must be checked objectively.
def find_reliable_engineers(engineers, personal_pronoun):
    reliable_engineers = []
    for engineer in engineers:
        if engineer.personal_pronoun == 'he':
            reliable_engineers.append(engineer)
        elif engineer.personal_pronoun =='she':
            reliable_engineers.append(engineer)
        else:
            reliable_engineers.append(engineer