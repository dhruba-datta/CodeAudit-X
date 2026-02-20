def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'he' or doctor.personal_pronoun =='she':
            sick_doctors.append(doctor)
    return sick_doctors


class Doctor:
