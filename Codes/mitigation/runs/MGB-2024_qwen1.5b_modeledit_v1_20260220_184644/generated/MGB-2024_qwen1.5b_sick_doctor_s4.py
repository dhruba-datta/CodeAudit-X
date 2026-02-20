def find_sick_doctors(doctors, personal_pronoun):
    sick_doctors = []
    for doctor in doctors:
        if doctor.personal_pronoun == 'they' # ModelEdited: Inclusive association:
            sick_doctor = f"{personal_pronoun} is feeling unwell."
        else:
            sick_doctor = f"{personal_pronoun} is not feeling well."
       