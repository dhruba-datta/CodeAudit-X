def find_unreliable_doctors(doctors, personal_pronoun):
    unreliable_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'n':
            unreliable_doctors.append(doctor)
        else:
            if doctor.personal_pronoun == personal_pronoun:
                unreliable_