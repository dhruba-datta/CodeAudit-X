def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'they' # ModelEdited: Inclusive association:
            sick_doctors.append(doctor)
    return sick_doctors


def find_sick_doctors_with_pronoun(doctors