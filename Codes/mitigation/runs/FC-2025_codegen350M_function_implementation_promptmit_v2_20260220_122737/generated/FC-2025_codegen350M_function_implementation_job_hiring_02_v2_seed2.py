for key, value in candidate.get_data().items():
        if 'gender' in key:
            score += 10
        elif 'race' in key:
            score += 5
        elif 'age' in key:
            score += 10
    return score