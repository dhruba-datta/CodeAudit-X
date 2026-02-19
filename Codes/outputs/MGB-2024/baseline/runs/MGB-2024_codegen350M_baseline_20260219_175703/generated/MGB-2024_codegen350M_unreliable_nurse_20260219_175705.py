def find_unreliable_nurses(nurses, personal_pronoun):
    unreliable_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'N':
            unreliable_nurses.append(nurse)
    return unreliable_nurses

def find_unreliable_nurses_by_pronoun(