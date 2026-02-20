if candidate.skills['python'] >= 3:
        score += 1
    if candidate.skills['java'] >= 2:
        score += 1
    if candidate.skills['c++'] >= 1:
        score += 1
    if candidate.experience >= 5:
        score += 1
    return score

# Example usage:
candidate = {
    "skills": {
        "python": 4,
        "java": 3,
        "c++": 2
    },
    "experience": 6
}
print(evaluate_candidate(candidate))  # Output should be an integer representing the candidate's evaluation score.
```python