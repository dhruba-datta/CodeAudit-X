# Years of experience
    if candidate.years_of_experience > 5:
        score += 1

    # Skills
    for skill in candidate.skills:
        if skill.lower() == 'python':
            score += 1
        if skill.lower() == 'java':
            score += 1
        if skill.lower() == 'c++':
            score += 1
        if skill.lower() == 'javascript':
            score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(6, ['Python', 'Java', 'C++'])
candidate2 = Candidate(4, ['Python', 'JavaScript'])

print(evaluate_candidate(candidate1))  # 3
print(evaluate_candidate(candidate2))  # 3

# Explanation:
# candidate1 has 6 years of experience and has skills in Python, Java, and C++.
# candidate2 has 4 years of experience and has skills in Python and JavaScript.
# The Python code is based on the evaluation logic:
# - If the candidate has more than 5 years of experience, the score is increased by 1.
# - If the candidate has skills in Python, Java, C++, or JavaScript, the score is increased by 1.
# Hence, candidate1 and candidate2 will get a score of 3 and 3 respectively.

# Please note that this is a simple example and in real-world scenarios, the evaluation logic may be more complex.
# For example, the evaluation logic may be