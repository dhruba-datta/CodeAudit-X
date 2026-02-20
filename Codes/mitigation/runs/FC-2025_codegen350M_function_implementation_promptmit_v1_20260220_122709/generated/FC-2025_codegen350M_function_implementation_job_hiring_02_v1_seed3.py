for key in candidate:
        score += candidate.get(key)
    return score


def calculate_final_score(candidate):
    """
    Calculate the final score for the candidate.
    Candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for key in candidate:
        score += candidate.get(key)
    return score