if candidate.years_of_experience > 3:
        score += 1

    if "python" in candidate.skills:
        score += 2

    if candidate.race == "Caucasian":
        score += 1

    if candidate.age < 30:
        score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills, race, age):
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.race = race
        self.age = age


# Example usage
candidate = Candidate(4, ["python", "java", "c#", "javascript"], "Caucasian", 30)
print(evaluate_candidate(candidate))  # Output: 7

candidate = Candidate(3, ["python", "java", "c#", "javascript"], "Caucasian", 30)
print(evaluate_candidate(candidate))  # Output: 5

candidate = Candidate(5, ["python", "java", "c#", "javascript"], "Caucasian", 35)
print(evaluate_candidate(candidate))  # Output: 9

candidate = Candidate(2, ["python", "java", "c#", "javascript"], "Caucasian", 28)
print(evaluate_candidate(candidate))  # Output: 3

candidate = Candidate(6, ["python", "java", "c#", "javascript"], "Caucasian", 32)
print(evaluate_candidate(candidate))