def find_unreliable_teachers(teachers, personal_pronoun):
    unreliable_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'unreliable' and teacher.personal_pronoun!= personal_pronoun:
            unreliable_teachers.append(teacher)
    return unreliable_teachers

