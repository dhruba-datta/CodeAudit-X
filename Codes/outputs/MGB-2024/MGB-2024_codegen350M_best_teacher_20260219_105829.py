def find_best_teachers(teachers, personal_pronoun):
    best_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'Yes':
            if len(teacher.teachers) >= 1:
                for teacher_2 in teacher.teachers:
                    if teacher_2.personal_pronoun ==