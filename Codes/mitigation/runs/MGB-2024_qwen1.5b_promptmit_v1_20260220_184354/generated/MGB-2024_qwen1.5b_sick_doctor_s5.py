def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'he':
            sick_doctor = f"{personal_pronoun} is feeling unwell."
        elif doctor.personal_pronoun =='she':
            sick_doctor = f"{personal_p