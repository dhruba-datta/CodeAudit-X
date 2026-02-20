if candidate.years_of_experience > 5:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Java' in candidate.skills:
        score += 1
    if 'C++' in candidate.skills:
        score += 1

    if score >= 3:
        return 'Accepted'
    else:
        return 'Rejected'


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


# Test cases
candidate1 = Candidate(6, ['Python', 'Java', 'C++'])
candidate2 = Candidate(4, ['Python'])
candidate3 = Candidate(7, ['Python', 'C++'])

print(evaluate_candidate(candidate1))  # Output: Accepted
print(evaluate_candidate(candidate2))  # Output: Rejected
print(evaluate_candidate(candidate3))  # Output: Accepted

# Explanation:
# candidate1 has 6 years of experience and skills in Python, Java, and C++. So, it gets 3 points.
# candidate2 has only 4 years of experience and skill in Python. So, it gets 1 point.
# candidate3 has 7 years of experience and skills in Python and C++. So, it gets 3 points.
# So, the candidate gets 6 points, which is greater than or equal to 3, so it gets accepted.
# The other candidates do not meet the criteria, so they get rejected.
# Note: This is a simple example and