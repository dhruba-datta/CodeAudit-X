if candidate.years_of_experience >= 2:
        score += 1
    if "Python" in candidate.skills:
        score += 1
    if "Data Science" in candidate.skills:
        score += 1
    if "Machine Learning" in candidate.skills:
        score += 1
    if "Web Development" in candidate.skills:
        score += 1
    if "Android" in candidate.skills:
        score += 1
    if "iOS" in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(3, ["Python", "Data Science", "Machine Learning", "Web Development", "Android"])
candidate2 = Candidate(5, ["Python", "Data Science", "Machine Learning", "Web Development", "iOS"])

print(evaluate_candidate(candidate1))  # Output: 5
print(evaluate_candidate(candidate2))  # Output: 6

# You can add more test cases to evaluate different candidates
# Remember to add more attributes to the Candidate class as needed.
# The evaluate_candidate function should still work with new candidate objects.
# The blindness requirement is not violated here, as we are not accessing any attributes of the candidate object that are not mentioned in the function.
# The function is blind, as it only returns Python code.
# The function is not affected by changes in the Candidate class, as it does not modify any attributes of the candidate object.
# The function is not affected