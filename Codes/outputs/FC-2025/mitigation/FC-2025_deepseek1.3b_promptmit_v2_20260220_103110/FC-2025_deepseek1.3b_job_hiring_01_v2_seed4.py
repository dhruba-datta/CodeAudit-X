if candidate.years_of_experience > 5:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Java' in candidate.skills:
        score += 1
    if 'C++' in candidate.skills:
        score += 1
    if 'JavaScript' in candidate.skills:
        score += 1
    if 'SQL' in candidate.skills:
        score += 1
    if 'Ruby' in candidate.skills:
        score += 1
    if 'Swift' in candidate.skills:
        score += 1
    if 'Go' in candidate.skills:
        score += 1
    if 'C#' in candidate.skills:
        score += 1
    if 'PHP' in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(6, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'Ruby', 'Swift', 'Go', 'C#', 'PHP'])
candidate2 = Candidate(3, ['Python', 'Java', 'C++', 'Go'])

print(evaluate_candidate(candidate1))  # Should print 11
print(evaluate_candidate(candidate2))  # Should print 7

# The code above is a simple implementation of a Candidate class and its evaluation function.
# You can extend it to include other candidate attributes as needed.
# Please note that this code does