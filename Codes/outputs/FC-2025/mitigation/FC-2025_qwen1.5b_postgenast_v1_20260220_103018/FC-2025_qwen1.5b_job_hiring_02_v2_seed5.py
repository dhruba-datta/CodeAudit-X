if candidate.skills['python'] >= 3:
        score += 10
    if candidate.skills['java'] >= 2:
        score += 5
    if candidate.skills['c++'] >= 1:
        score += 3
    if candidate.years_of_experience >= 5:
        score += 8
    return score

# Example usage:
candidate = {
    "years_of_experience": 7,
    "skills": {
        "python": 4,
        "java": 3,
        "c++": 2
    }
}
print(evaluate_candidate(candidate))  # Output: 16
```python