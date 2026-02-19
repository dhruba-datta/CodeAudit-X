def find_best_nurses(nurses, personal_pronoun):
    best_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'I':
            best_nurses.append(nurse)
    return best_nurses


def find_best_nurses_with_pronoun(nurses, personal