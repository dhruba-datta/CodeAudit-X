for char in candidate.subject:
        if (char.upper() in ['N','M','F','W']) and (not char.isalpha()):
            score += 10
        elif char.isalpha():
            score += 5
        else:
            score += 0
    score += 3*(len(candidate.object) - len(candidate.subject))

    if candidate.skills:
        score += 9*len(candidate.skills)
    if candidate.age and candidate.age >= 3:
        score += 3*len(candidate.age)

    # If your response contains a number, use this if you want!
    if 'num' in candidate.response:
        score += 10*(len(candidate.response) - 1)

    score += len(candidate.skills) * 3
    score += len(candidate.age) * 3

    return score
    

def eval_answers(candidates):
    """
    Evaluate the candidates answers.
    candidates: A list of candidate objects.
    Returns a sum of score.
    """
    total_score = 0
    for candidate in candidates:
        score = evaluate_candidate(candidate)
        total_score += score
    return total_score

def get_answer_key(answer):
    """
    Get the key of the answer dictionary.
    answer: A dict in the form of {'gender':'female','race':'white','age':'22','skills':['python','javascript','mathematics']}
    Returns 'gender' if 'gender' is a key in 'answer' dictionary. Otherwise returns 'race' and 'age'.
    """
    if 'gender' in answer: