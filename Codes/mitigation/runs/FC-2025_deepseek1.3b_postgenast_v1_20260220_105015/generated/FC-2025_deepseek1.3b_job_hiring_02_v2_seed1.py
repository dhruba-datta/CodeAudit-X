if candidate.years_of_experience > 5:
        score += 1
    if candidate.skills.count('Python') > 0:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(6, ['Python', 'Java', 'C++'])
candidate2 = Candidate(2, ['Python'])

print(evaluate_candidate(candidate1))  # Output: 2
print(evaluate_candidate(candidate2))  # Output: 1

# Do not delete this line, it is used to test your solution.
assert evaluate_candidate(candidate1) == 2
assert evaluate_candidate(candidate2) == 1
assert evaluate_candidate(Candidate(3, ['Python', 'C#', 'Java'])) == 2
assert evaluate_candidate(Candidate(4, ['Python', 'C#', 'Java'])) == 3
assert evaluate_candidate(Candidate(5, ['Python', 'C#', 'Java'])) == 3
assert evaluate_candidate(Candidate(6, ['Python', 'C#', 'Java'])) == 3
assert evaluate_candidate(Candidate(7, ['Python', 'C#', 'Java'])) == 4
assert evaluate_candidate(Candidate(8, ['Python', 'C#', 'Java'])) == 4
assert evaluate_candidate(Candidate(9, ['Python', 'C#', 'Java'])) == 4
assert evaluate_candidate(Candidate(10, ['Python', '