if candidate.years_of_experience > 5:
        score += 1

    if 'Python' in candidate.skills:
        score += 1

    if 'JavaScript' in candidate.skills:
        score += 1

    if 'C++' in candidate.skills:
        score += 1

    return score


def evaluate_engineer_team(team):
    """
    Evaluate an engineer team.
    team: A list of candidate objects.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    total_score = 0

    for candidate in team:
        total_score += evaluate_candidate(candidate)

    return total_score


def evaluate(candidate_list):
    """
    Evaluate a list of software engineer candidates.
    candidate_list: A list of candidate objects.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    total_score = 0

    for candidate in candidate_list:
        total_score += evaluate_candidate(candidate)

    return total_score


def main():
    pass


if __name__ == "__main__":
    main()

#evaluate.py
class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


def evaluate_candidate(candidate):
    """
    Evaluate a software engineer candidate.