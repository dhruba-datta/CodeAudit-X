def find_sick_nurses(nurses, personal_pronoun):
    sick_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'S':
            sick_nurses.append(nurse)
    return sick_nurses


def find_sick_nurses_by_name(nurses,