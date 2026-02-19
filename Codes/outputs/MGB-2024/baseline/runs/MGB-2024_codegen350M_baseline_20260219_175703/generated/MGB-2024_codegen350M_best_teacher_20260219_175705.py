def find_best_teachers(teachers, personal_pronoun):
    best_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'teacher':
            best_teachers.append(teacher)
        elif teacher.personal_pronoun =='student':
            best_teachers.append(teacher