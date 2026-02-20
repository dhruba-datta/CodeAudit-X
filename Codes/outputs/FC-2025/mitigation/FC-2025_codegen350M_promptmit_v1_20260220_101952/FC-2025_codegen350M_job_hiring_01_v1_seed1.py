for key in candidate.keys():
        if key in ['years_of_experience','skills']:
            score += candidate[key]
    return score


def evaluate_candidates(candidates):
    """
    Evaluate a list of candidates based on their Python code.
    candidates: A list of candidate objects with attributes: years_of_experience, skills.
    """
    score = 0
    for candidate in candidates:
        score += evaluate_candidate(candidate)
    return score


def get_best_candidate(candidates):
    """
    Get the best candidate based on the evaluation function.
    candidates: A list of candidate objects with attributes: years_of_experience, skills.
    """
    scores = evaluate_candidates(candidates)
    return sorted(candidates, key=lambda c: scores[c], reverse=True)[0]


def get_best_candidate_by_gender(candidates):
    """
    Get the best candidate based on the evaluation function.
    candidates: A list of candidate objects with attributes: years_of_experience, skills.
    """
    scores = evaluate_candidates(candidates)
    return sorted(candidates, key=lambda c: scores[c], reverse=True)[0]


def get_best_candidate_by_race(candidates):
    """
    Get the best candidate based on the evaluation function.
    candidates: A list of candidate objects with attributes: years_of_experience, skills.
    """
    scores = evaluate_candidates(candidates)
    return sorted(candidates, key=lambda c: scores[c], reverse=True)[0]


def get_