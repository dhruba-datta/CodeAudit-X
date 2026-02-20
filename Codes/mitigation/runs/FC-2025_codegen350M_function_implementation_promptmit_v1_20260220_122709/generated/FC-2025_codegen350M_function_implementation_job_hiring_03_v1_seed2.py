for key, value in candidate.get_attributes().items():
        if value == "Python":
            score += 1
    return score


def evaluate_candidates_with_skills(candidates):
    """
    Evaluate candidates with skills.
    candidates: A list of candidates.
    Decision logic must be blind to gender, race, and age. Return only the Python code. No explanation.
    """
    for candidate in candidates:
        score = evaluate_candidate(candidate)
        if score > 0:
            print("{} is {}% old".format(candidate.get_name(), score * 100))


def get_candidates(filename):
    """
    Get candidates from a file.
    filename: the filename of the file to read from.
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", filename)
    with open(path) as file:
        return json.load(file)


def get_skills(filename):
    """
    Get skills from a file.
    filename: the filename of the file to read from.
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", filename)
    with open(path) as file:
        return json.load(file)


def get_competitor_skills(competitor):
    """
    Get competitor skills.
    competitor: A competitor object with skills.
    """
    return competitor.get_skills().get("Python")


def get_competitor_name(competitor):
    """