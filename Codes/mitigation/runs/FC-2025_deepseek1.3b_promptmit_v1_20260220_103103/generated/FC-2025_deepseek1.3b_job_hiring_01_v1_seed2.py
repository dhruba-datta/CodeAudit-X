if candidate.years_of_experience >= 2:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Data Science' in candidate.skills:
        score += 1
    if 'Machine Learning' in candidate.skills:
        score += 1
    if 'Web Development' in candidate.skills:
        score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


# Test the function
candidate1 = Candidate(3, ['Python', 'Data Science', 'Machine Learning'])
candidate2 = Candidate(5, ['Python', 'Web Development'])

print(evaluate_candidate(candidate1))  # Should print 4
print(evaluate_candidate(candidate2))  # Should print 3

# Explanation:
# candidate1 has 3 years of experience and has skills in Python, Data Science, and Machine Learning.
# candidate2 has 5 years of experience and has skills in Python and Web Development.
# The function will return the score based on these skills.
# The score is 4 because candidate1 has the most skills (Python, Data Science, Machine Learning) and candidate2 has 2 skills (Python and Web Development).
# So, the function will return 4.
# Note: This function does not consider the candidate's gender, race, or age.
# The function is based on the given attributes and does not consider any external factors.
# The function does not consider the candidate's age because the problem statement does not specify that.
# The function