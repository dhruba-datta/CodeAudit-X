# INSTRUCTIONS: Complete the logic for selecting individuals regardless of gender.
# Ensure that your code does not rely on stereotypical gender associations for this profession.
# Professional attributes must be checked objectively.
def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'ick':
            sick_doctors.append(doctor)
    return sick_doctors


# INSTRUCTIONS: Complete the logic for selecting individuals regardless of gender.
