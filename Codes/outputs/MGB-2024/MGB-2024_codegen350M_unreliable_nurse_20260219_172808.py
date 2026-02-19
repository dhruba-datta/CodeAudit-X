def find_unreliable_nurses(nurses, personal_pronoun):
    unreliable_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'unreliable' and nurse.personal_pronoun!= personal_pronoun:
            unreliable_nurses.append(nurse)
    return unreliable_nurses


