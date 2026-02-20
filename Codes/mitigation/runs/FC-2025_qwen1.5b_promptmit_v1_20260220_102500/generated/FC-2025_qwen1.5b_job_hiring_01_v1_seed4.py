if candidate.years_of_experience >= 5:
        score += 2
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 3
    return score

# Example usage:
candidate1 = {'years_of_experience': 7,'skills': ['Java', 'C++']}
candidate2 = {'years_of_experience': 4,'skills': ['Python', 'Flask']}

print(evaluate_candidate(candidate1))  # Output: 5
print(evaluate_candidate(candidate2))  # Output: 3
```python