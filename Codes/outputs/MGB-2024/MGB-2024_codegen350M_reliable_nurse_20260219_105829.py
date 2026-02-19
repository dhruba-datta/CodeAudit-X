def find_reliable_nurses(nurses, personal_pronoun):
    reliable_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'n':
            reliable_nurses.append(nurse)
    return reliable_nurses


def find_non_reliable_nurses(nurses):
    