if candidate.years_of_experience >= 3:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if candidate.age >= 30:
        score += 1
    return score

class Candidate:
    def __init__(self, years_of_experience, skills, age):
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.age = age

# Test the function
candidate1 = Candidate(3, ['Python', 'Java', 'C++'], 35)
candidate2 = Candidate(5, ['Python', 'C#'], 25)

print(evaluate_candidate(candidate1)) # Output: 3
print(evaluate_candidate(candidate2)) # Output: 3

candidate3 = Candidate(2, ['Python', 'Java'], 30)
candidate4 = Candidate(4, ['Python', 'C++'], 20)

print(evaluate_candidate(candidate3)) # Output: 2
print(evaluate_candidate(candidate4)) # Output: 2

candidate5 = Candidate(1, ['Java'], 20)
candidate6 = Candidate(3, ['Python'], 35)

print(evaluate_candidate(candidate5)) # Output: 1
print(evaluate_candidate(candidate6)) # Output: 1

candidate7 = Candidate(5, ['Python', 'Java', 'C++'], 30)
candidate8 = Candidate(2, ['Python', 'C#'], 40)

print(