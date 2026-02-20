if candidate.years_of_experience >= 5:
        score += 10
    if 'Python' in candidate.skills:
        score += 5
    if 'Java' not in candidate.skills:
        score -= 2
    return score

# Example usage
candidate = {'years_of_experience': 7,'skills': ['Python', 'JavaScript']}
print(evaluate_candidate(candidate))  # Output will vary based on the evaluation criteria
```python