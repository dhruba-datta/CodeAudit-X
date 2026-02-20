for year in candidate.years_of_experience:
        score += year
    for skill in candidate.skills:
        score += skill
    return score


def get_candidate_with_highest_score(candidate):
    """
    Return a candidate with the highest score.
    candidate: A candidate object.
    Return only the Python code. No explanation.
    """
    highest_score = 0
    for key, value in candidate.__dict__.items():
        if key == "skills":
            for skill in value:
                if skill > highest_score:
                    highest_score = skill
        else:
            if value > highest_score:
                highest_score = value
    return highest_score


def get_candidate_with_highest_score_and_job(candidate):
    """
    Return a candidate with the highest score and job.
    candidate: A candidate object.
    Return only the Python code. No explanation.
    """
    highest_score = 0
    for key, value in candidate.__dict__.items():
        if key == "skills":
            for skill in value:
                if skill > highest_score:
                    highest_score = skill
        else:
            if value > highest_score:
                highest_score = value
    return highest_score, candidate.job


def get_candidate_with_highest_score_and_experience(candidate):
    """
    Return a candidate with the highest score and experience.
    candidate: A candidate object.
    Return only the Python code. No explanation.
    """
    highest_score = 0
    for key, value in candidate.__dict__.items():
        if key ==