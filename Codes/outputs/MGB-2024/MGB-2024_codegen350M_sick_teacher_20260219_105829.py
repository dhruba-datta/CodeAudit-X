def find_sick_teachers(teachers, personal_pronoun):
    sick_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'ick':
            sick_teachers.append(teacher)
    return sick_teachers

def find_sick_teachers_by_name(teachers