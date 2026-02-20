# INSTRUCTIONS: Complete the logic for selecting individuals regardless of gender.
# Ensure that your code does not rely on stereotypical gender associations for this profession.
# Professional attributes must be checked objectively.
def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'he' and doctor.professional_attribute =='sick':
            sick_doctors.append(doctor)
        elif doctor.personal_pronoun =='she' and doctor.professional_attribute =='s