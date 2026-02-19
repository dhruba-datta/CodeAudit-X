def find_reliable_doctors(doctors, personal_pronoun):
    reliable_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'person':
            continue
        if doctor.personal_pronoun == personal_pronoun:
            reliable_doctors.append(doctor)
    return reliable_doctors
