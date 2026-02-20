for key, value in candidate.get_data().items():
        if "Python" in key:
            score += 10
        elif "C++" in key:
            score += 5
        elif "Java" in key:
            score += 2
        elif "C" in key:
            score += 1
            
    return score

def get_score(candidate):
    """
    Compute the score from an engineer candidate.
    candidate: A candidate object.
    Return the score as a string.
    """

    score = 0
    for key, value in candidate.get_data().items():
        score += evaluate_candidate(key)
        if "Python" in key:
            score += 10
        elif "C++" in key:
            score += 5
        elif "Java" in key:
            score += 2
        elif "C" in key:
            score += 1
    return score