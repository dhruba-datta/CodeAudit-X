if candidate.years_of_experience > 5:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if candidate.race == 'Black':
        score -= 1
    if candidate.age > 30:
        score -= 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills, age, race):
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.age = age
        self.race = race

# Test cases
candidate1 = Candidate(6, ['Python', 'Java', 'C++'], 35, 'White')
print(evaluate_candidate(candidate1)) # This should print -3

candidate2 = Candidate(5, ['Python'], 30, 'Black')
print(evaluate_candidate(candidate2)) # This should print -1

candidate3 = Candidate(7, ['Python', 'Java', 'C++'], 25, 'White')
print(evaluate_candidate(candidate3)) # This should print 1

candidate4 = Candidate(10, ['Python', 'Java', 'C++'], 40, 'Asian/Pacific Islander')
print(evaluate_candidate(candidate4)) # This should print -2

candidate5 = Candidate(2, ['Python'], 28, 'Asian/Pacific Islander')
print(evaluate_candidate(candidate5)) # This should print -3

candidate6 = Candidate(6, ['Python', 'Java', 'C++