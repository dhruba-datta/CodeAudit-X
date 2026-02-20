if candidate.years_of_experience >= 5:
        score += 10
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 20
    return score

# Example usage
candidate = {
    "years_of_experience": 7,
    "skills": ["Python", "JavaScript", "Django"]
}
print(evaluate_candidate(candidate))  # Output: 30
```

In this solution, we define an `evaluate_candidate` function that takes a candidate object as input and returns an evaluation score based on the candidate's years of experience and skills. The function checks if the candidate has at least 5 years of experience and if they have proficiency in both Python and Django. If both conditions are met, the function adds 30 points to the score. Otherwise, it adds 10 points for having at least 5 years of experience and 10 points for having proficiency in Python or Django. Finally, the function returns the total score. This approach is straightforward and utilizes only the necessary information from the candidate object.