def find_reliable_nurses(nurses, personal_pronoun):
    reliable_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'I':
            reliable_nurses.append(nurse)
        elif nurse.personal_pronoun == 'you':
            reliable_nurses.append(n