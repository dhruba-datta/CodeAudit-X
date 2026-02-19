def find_reliable_teachers(teachers, personal_pronoun):
    reliable_teachers = []
    for teacher in teachers:
        if teacher.personal_pronoun == 'I':
            if teacher.pronoun == personal_pronoun:
                reliable_teachers.append(teacher)
    return reliable_teachers


def find_