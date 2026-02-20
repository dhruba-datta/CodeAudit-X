if candidate.years_of_experience > 3:
        score += 1

    if "python" in candidate.skills:
        score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(4, ["python", "java", "c++"])
candidate2 = Candidate(2, ["python"])
candidate3 = Candidate(5, ["python", "javascript"])

print(evaluate_candidate(candidate1))  # 1
print(evaluate_candidate(candidate2))  # 1
print(evaluate_candidate(candidate3))  # 2

# Output:
# 1
# 1
# 2
```

This code defines a `Candidate` class with `years_of_experience` and `skills` attributes. The `evaluate_candidate` function then uses these attributes to evaluate a candidate. The function returns a score based on the candidate's experience and the candidate's skills.