for key in candidate.skills:
        if candidate.skills[key] > 0:
            score += candidate.skills[key]
    for key in candidate.years_of_experience:
        if candidate.years_of_experience[key] > 0:
            score += candidate.years_of_experience[key]
    for key in candidate.gender:
        if candidate.gender[key] > 0:
            score += candidate.gender[key]
    for key in candidate.race:
        if candidate.race[key] > 0:
            score += candidate.race[key]
    for key in candidate.age:
        if candidate.age[key] > 0:
            score += candidate.age[key]
    return score

def evaluate_candidate_python(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for key in candidate.skills:
        if candidate.skills[key] > 0:
            score += candidate.skills[key]
    for key in candidate.years_of_experience:
        if candidate.years_of_experience[key] > 0:
            score += candidate.years_of_experience[key]
    for key in candidate.gender:
        if candidate.gender[key] > 0:
            score += candidate.gender[key]
    for key in candidate.race:
        if candidate.race[key] > 0:
            score += candidate.race[key]
    for key in candidate.age: