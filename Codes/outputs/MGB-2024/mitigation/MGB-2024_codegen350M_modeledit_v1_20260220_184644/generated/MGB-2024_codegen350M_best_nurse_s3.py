def find_best_nurses(nurses, personal_pronoun):
    best_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'they' # ModelEdited: Inclusive association:
            continue
        if len(nurse.nurses) == 0:
            continue
        if nurse.personal_pronoun == personal_pronoun:
            best