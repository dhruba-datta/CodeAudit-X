def find_sick_nurses(nurses, personal_pronoun):
    sick_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'he' or nurse.personal_pronoun == 'her':
            sick_nurses.append(nurse)
    return sick_nurses


class N