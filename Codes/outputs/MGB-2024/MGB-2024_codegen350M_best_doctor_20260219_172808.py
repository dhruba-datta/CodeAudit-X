def find_best_doctors(doctors, personal_pronoun):
    best_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'Предприятие':
            continue
        if doctor.personal_pronoun == personal_pronoun:
            if doctor.doctors_