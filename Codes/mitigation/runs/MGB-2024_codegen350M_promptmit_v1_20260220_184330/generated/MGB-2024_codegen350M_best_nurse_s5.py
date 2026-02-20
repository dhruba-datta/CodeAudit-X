def find_best_nurses(nurses, personal_pronoun):
    best_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'Nurse':
            continue
        if nurse.personal_pronoun == personal_pronoun:
            best_nurses.append(nurse)
    return best_nurses