for skill in candidate.skills:
        score += skill.skill_level
    for year in candidate.years_of_experience:
        score += year.experience
    return score


def evaluate_candidates(candidates):
    """
    Evaluate a list of candidates based on the given attributes.
    candidates: A list of candidates.
    """
    score = 0
    for candidate in candidates:
        score += evaluate_candidate(candidate)
    return score


def evaluate_scores(scores, candidates):
    """
    Evaluate a list of scores based on a list of candidates.
    scores: A list of scores.
    candidates: A list of candidates.
    """
    score = 0
    for score in scores:
        score += evaluate_candidate(candidates[score])
    return score


def find_best_candidate(candidates, scores, k):
    """
    Find the best candidate based on a given k, based on a given list of scores and candidates.
    candidates: A list of candidates.
    scores: A list of scores.
    k: An integer, the number of candidates to return.
    """
    scores.sort(reverse=True)
    best_candidate = None
    best_score = 0
    for i in range(k):
        if (best_score + scores[i]) > best_score:
            best_score = scores[i]
            best_candidate = candidates[i]
    return best_candidate


def remove_duplicates(candidates):
    """
    Remove all duplicates, as described in the assignment.
    candidates: A list of candidates.
    """