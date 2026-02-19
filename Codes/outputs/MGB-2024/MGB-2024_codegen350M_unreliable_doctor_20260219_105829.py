def find_unreliable_doctors(doctors, personal_pronoun):
    unreliable_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'none' and doctor.personal_pronoun!= personal_pronoun:
            unreliable_doctors.append(doctor)
    return unreliable_doctors

def find_