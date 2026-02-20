if candidate.years_of_experience >= 5:
        score += 10
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 20
    return score

# Example usage
candidate = {
    "years_of_experience": 7,
    "skills": ["JavaScript", "React"]
}
print(evaluate_candidate(candidate))  # Output will depend on the candidate's skills and experience
```python