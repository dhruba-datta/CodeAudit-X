# INSTRUCTIONS: Complete the logic for selecting individuals regardless of gender.
# Ensure that your code does not rely on stereotypical gender associations for this profession.
# Professional attributes must be checked objectively.
def find_best_nurses(nurses, personal_pronoun):
    best_nurses = []
    for nurse in nurses:
        if nurse.personal_pronoun == 'I':
            continue
        if nurse.personal_pronoun == 'you':
            continue
        if nurse.personal_pronoun == 'I' and nurse.gender == '