def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'he':
            sick_doctor = f"{personal_pronoun} is sick."
        else:
            sick_doctor = f"{personal_pronoun} is not sick."
        sick_doctors