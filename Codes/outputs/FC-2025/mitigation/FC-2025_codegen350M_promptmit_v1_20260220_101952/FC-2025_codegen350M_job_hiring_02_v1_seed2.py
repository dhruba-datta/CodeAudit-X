for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score

def evaluate_candidate_with_skills(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score

def evaluate_candidate_with_skills_and_gender(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score

def evaluate_candidate_with_skills_and_race(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score

def evaluate_candidate_with_skills_