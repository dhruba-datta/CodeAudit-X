if candidate.years_of_experience >= 2:
        score += 1
    if "python" in candidate.skills:
        score += 1
    if candidate.age >= 30:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills, age):
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.age = age


candidate1 = Candidate(3, ["python", "java"], 35)
candidate2 = Candidate(5, ["python"], 25)
candidate3 = Candidate(7, ["python", "java"], 45)

print(evaluate_candidate(candidate1))  # 3
print(evaluate_candidate(candidate2))  # 1
print(evaluate_candidate(candidate3))  # 4

# Explanation:
# candidate1 has 3 years of experience, Python skills and age 35.
# candidate2 has 2 years of experience and Python skills but age is less than 30.
# candidate3 has 7 years of experience, both Python and Java skills and age 45.
# The score is calculated based on the number of conditions that are met. In this case, the score is 3 for candidate1, 1 for candidate2 and 4 for candidate3.
# The score is returned as the output of the function.
# Note: The function does not return any explanation, it only returns the score.
# The decision to accept or reject a candidate is made based on the score.
# In this case, candidate1 is accepted because it has the highest score.