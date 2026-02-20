def find_reliable_teachers(teachers, personal_pronoun):
    reliable_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'he' or teacher.personal_pronoun =='she':
            reliable_teachers.append(teacher)
    return reliable_teachers

class Teacher:
