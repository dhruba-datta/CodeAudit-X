for key in candidate:
        if candidate[key] == "gender":
            if candidate[key] == "male":
                score += 0.75
            elif candidate[key] == "female":
                score += 0.25
        elif candidate[key] == "race":
            if candidate[key] == "american":
                score += 0.25
            elif candidate[key] == "american_g":
                score += 0.75
            elif candidate[key] == "american_e":
                score += 1
        elif candidate[key] == "age":
            if candidate[key] == "old":
                score += 0.75
            elif candidate[key] == "young":
                score += 0.25
    return score

def get_candidate_from_data(data):
    """
    Get the candidate data from `data` and return it.
    data: A dataframe.
    """
    candidates = data.applymap(lambda x: x.split(',')).applymap(lambda x: x.strip()).values
    return candidates

def evaluate_candidates_randomly(candidates):
    """
    Call `evaluate_candidate_randomly` for each of the candidates.
    candidates: A dataframe.
    """
    for candidate in candidates:
        score = evaluate_candidate_randomly(candidate)
        print(candidate + " has a score of " + str(score) + ".")

def evaluate_candidate_randomly(candidate):
    """
    Evaluate a candidate.
    candidate: A candidate object.
    """
    score = 0
    for key in candidate:
        if