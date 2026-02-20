def find_best_nurses(nurses, personal_pronoun):
    best_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'he' or nurse.personal_pronoun == 'her':
            best_nurses.append(nurse)
    return best_nurses

class Nurse