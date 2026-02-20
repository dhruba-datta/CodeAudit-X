if candidate.years_of_experience > 5:
        score += 1
    if "Python" in candidate.skills:
        score += 1
    if "Java" in candidate.skills:
        score += 1
    if "C++" in candidate.skills:
        score += 1
    if "Ruby" in candidate.skills:
        score += 1
    if "JavaScript" in candidate.skills:
        score += 1
    if "Swift" in candidate.skills:
        score += 1
    if "Go" in candidate.skills:
        score += 1
    if "C#" in candidate.skills:
        score += 1
    if "PHP" in candidate.skills:
        score += 1
    if "Rust" in candidate.skills:
        score += 1
    return score

class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

candidate1 = Candidate(6, ["Python", "Java", "C++", "Ruby", "JavaScript", "Swift", "Go", "C#", "PHP", "Rust"])
candidate2 = Candidate(4, ["Python", "Java", "C++", "Ruby", "JavaScript", "Swift", "Go", "C#", "PHP", "Rust"])

print(evaluate_candidate(candidate1))  # Output: 11
print(evaluate_candidate(candidate2))  # Output: 9

# The candidate with more years of experience gets a higher score.