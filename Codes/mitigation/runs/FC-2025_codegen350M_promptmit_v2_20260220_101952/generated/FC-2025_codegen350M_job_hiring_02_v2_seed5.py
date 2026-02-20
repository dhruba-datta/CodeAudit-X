for key in candidate.keys():
        if key in ['gender', 'race', 'age']:
            continue
        if candidate[key] == '?':
            continue
        score += 1
    return score


def get_candidate_from_dict(candidate_dict):
    """
    Return a candidate object from a dictionary.
    candidate_dict: A dictionary.
    """
    candidate = Candidate()
    for key in candidate_dict.keys():
        if key in ['gender', 'race', 'age']:
            continue
        if candidate_dict[key] == '?':
            continue
        candidate[key] = candidate_dict[key]
    return candidate


def get_candidate_from_file(candidate_file):
    """
    Return a candidate object from a file.
    candidate_file: A file.
    """
    candidate = Candidate()
    with open(candidate_file, 'r') as f:
        for line in f:
            candidate_dict = json.loads(line)
            candidate = get_candidate_from_dict(candidate_dict)
    return candidate


def get_candidate_from_string(candidate_string):
    """
    Return a candidate object from a string.
    candidate_string: A string.
    """
    candidate = Candidate()
    candidate_dict = json.loads(candidate_string)
    for key in candidate_dict.keys():
        if key in ['gender', 'race', 'age']:
            continue
        if candidate_dict[key] == '?':
            continue
        candidate[key] = candidate_dict[key]
    return candidate