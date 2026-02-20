for year in candidate.years_of_experience:
        if year >= 10:
            score += 1
    for skill in candidate.skills:
        if skill.skill_type == "Python":
            score += 10
    return score

def evaluate_scores(candidate):
    """
    Evaluate the scores of the candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for year in candidate.years_of_experience:
        if year >= 10:
            score += 1
    for skill in candidate.skills:
        if skill.skill_type == "Python":
            score += 10
    return score

def get_most_common_skills(candidate):
    """
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    return candidate.skills.most_common(1)[0][0]