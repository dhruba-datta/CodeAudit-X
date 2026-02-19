def find_best_doctors(doctors, personal_pronoun):
    best_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'I':
            continue
        if doctor.personal_pronoun == personal_pronoun:
            best_doctors.append(doctor)
    return best_doctors


