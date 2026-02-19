def find_best_teachers(teachers, personal_pronoun):
    best_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'преподаватель':
            continue
        if teacher.personal_pronoun == personal_pronoun:
            best_teachers