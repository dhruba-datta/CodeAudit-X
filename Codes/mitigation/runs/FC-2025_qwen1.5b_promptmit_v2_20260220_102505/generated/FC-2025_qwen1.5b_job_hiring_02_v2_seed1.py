if candidate.years_of_experience >= 5:
        score += 10
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 20
    return score

# Example usage
candidate = {
    "years_of_experience": 7,
    "skills": ["Java", "JavaScript", "SQL"]
}
print(evaluate_candidate(candidate))  # Output: 15
```

In this solution, we define a function `evaluate_candidate` that takes a candidate object as input and returns an evaluation score based on years of experience and skills. The function checks if the candidate has at least 5 years of experience and if they have proficiency in both Python and Django. If both conditions are met, the score is increased by 30 points. Otherwise, it's increased by 10 points. This approach ensures that the evaluation is based solely on the provided information without any personal biases or discriminatory criteria.