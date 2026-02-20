if candidate.years_of_experience >= 5:
        score += 2
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 3
    return score

# Example usage:
candidate = {
    "years_of_experience": 7,
    "skills": ["Python", "Django", "JavaScript"]
}
print(evaluate_candidate(candidate))  # Output: 5
```python