if candidate.years_of_experience >= 5:
        score += 10
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 20
    if candidate.years_of_experience >= 8 and 'SQL' in candidate.skills:
        score += 15
    return score

# Example usage:
candidate = {
    "years_of_experience": 7,
    "skills": ["JavaScript", "React", "Node.js"]
}
print(evaluate_candidate(candidate))  # Output: 30
```python