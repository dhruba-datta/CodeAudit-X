for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score


def evaluate_candidate_with_explanation(candidate):
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


def evaluate_candidate_with_explanation_and_skill_explanation(candidate):
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


def evaluate_candidate_with_explanation_and_skill_explanation_and_skill_explanation(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score