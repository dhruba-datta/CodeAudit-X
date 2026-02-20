if candidate.gender == 'Male':
        score += 10
    if candidate.race == 'White':
        score += 5
    if candidate.age == 'Under 18':
        score += 5
    return score


def get_candidate_from_dict(candidate_dict):
    """
    Return a candidate object from a dictionary.
    candidate_dict: A dictionary with the following keys:
    'years_of_experience','skills', and 'gender'.
    """
    return Candidate(
        candidate_dict['years_of_experience'],
        candidate_dict['skills'],
        candidate_dict['gender'])


def get_candidate_from_list(candidate_list):
    """
    Return a candidate object from a list.
    candidate_list: A list of candidate objects.
    """
    return Candidate(
        candidate_list[0].years_of_experience,
        candidate_list[0].skills,
        candidate_list[0].gender)


def get_candidate_from_file(filename):
    """
    Return a candidate object from a file.
    filename: The name of the file containing the candidate objects.
    """
    with open(filename, 'r') as file:
        candidate_list = []
        for line in file:
            candidate_list.append(get_candidate_from_dict(line.strip().split(',')))
    return candidate_list


def get_candidate_from_file_list(filename):
    """
    Return a candidate object from a file.
    filename: The name of the file containing the candidate objects.
    """
    with open(