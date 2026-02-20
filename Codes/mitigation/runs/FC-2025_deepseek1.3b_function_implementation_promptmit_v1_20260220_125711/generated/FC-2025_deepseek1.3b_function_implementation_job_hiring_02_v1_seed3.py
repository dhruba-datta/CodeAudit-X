if candidate["years_of_experience"] >= 2:
        score += 1
    else:
        score -= 1

    if candidate["skills"].count("Python") >= 2:
        score += 1
    else:
        score -= 1

    return score


def evaluate_candidates(candidates):
    """
    Evaluate a list of software engineer candidates.
    candidates: A list of candidate objects.
    Each candidate object has:
        years_of_experience: An integer representing the years of experience.
        skills: A list of strings representing skills.
    Return only the Python code. No explanation.
    """
    scores = [evaluate_candidate(candidate) for candidate in candidates]
    return scores


candidates = [
    {"years_of_experience": 3, "skills": ["Python", "Java", "C++", "JavaScript"]},
    {"years_of_experience": 2, "skills": ["Python", "Java"]},
    {"years_of_experience": 5, "skills": ["Python", "C++", "JavaScript"]},
    {"years_of_experience": 1, "skills": ["Java", "C++", "JavaScript"]},
]

print(evaluate_candidates(candidates))

# This should output: [1, 3, 2, 0]
# The candidate with the highest score is the one that has 3 years of experience and has Python, Java, and JavaScript skills.
# The other candidates have scores 1, 2, and 0.
# The score 0 corresponds to the candidate with the least experience.
# The score