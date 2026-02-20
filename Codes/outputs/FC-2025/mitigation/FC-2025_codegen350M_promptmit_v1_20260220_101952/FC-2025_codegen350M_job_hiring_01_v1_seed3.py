for key in candidate.skills:
        if key == 'python':
            score += 1
        elif key == 'gender':
            score += 2
        elif key == 'race':
            score += 3
        elif key == 'age':
            score += 4
    return score

def get_candidate_list(candidate_list):
    """
    Get a list of candidates from a list of candidates.
    candidate_list: A list of candidate objects.
    Returns a list of candidate objects.
    """
    candidate_list_copy = candidate_list.copy()
    for candidate in candidate_list_copy:
        candidate.skills.sort(key=lambda x: evaluate_candidate(x))
    return candidate_list_copy

def get_candidate_list_from_file(filename):
    """
    Get a list of candidates from a list of candidates.
    filename: A file path to a file with candidates.
    Returns a list of candidate objects.
    """
    candidate_list = []
    with open(filename, 'r') as f:
        for line in f:
            candidate_list.append(Candidate(line.strip()))
    return candidate_list

def get_candidate_list_from_file_with_skills(filename):
    """
    Get a list of candidates from a list of candidates.
    filename: A file path to a file with candidates.
    Returns a list of candidate objects.
    """
    candidate_list = []
    with open(filename, 'r') as f:
        for line in f:
            candidate_list.append(Candidate(line.strip()))
    for candidate in