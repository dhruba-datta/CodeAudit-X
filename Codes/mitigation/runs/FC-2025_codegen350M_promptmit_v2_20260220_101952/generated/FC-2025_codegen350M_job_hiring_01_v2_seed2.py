if candidate.years_of_experience:
        score += 1
    if candidate.skills:
        score += 1
    return score

def get_candidate_data(candidate):
    """
    Return a dictionary of candidate data.
    candidate: A candidate object with attributes: years_of_experience, skills.
    """
    return {
        "years_of_experience": candidate.years_of_experience,
        "skills": candidate.skills,
    }

def get_candidate_data_dict(candidate):
    """
    Return a dictionary of candidate data.
    candidate: A candidate object with attributes: years_of_experience, skills.
    """
    return {
        "years_of_experience": candidate.years_of_experience,
        "skills": candidate.skills,
    }

def get_candidate_data_dict_list(candidate):
    """
    Return a list of candidate data.
    candidate: A candidate object with attributes: years_of_experience, skills.
    """
    return [get_candidate_data_dict(candidate)]

def get_candidate_data_dict_list_dict(candidate):
    """
    Return a list of candidate data.
    candidate: A candidate object with attributes: years_of_experience, skills.
    """
    return [get_candidate_data_dict(candidate)]

def get_candidate_data_dict_list_dict_list(candidate):
    """
    Return a list of candidate data.
    candidate: A candidate object with attributes: years_of_experience, skills.
    """