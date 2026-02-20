if candidate.years_of_experience > 5:
        score += 1

    if 'java' in candidate.skills:
        score += 1

    if 'python' in candidate.skills:
        score += 1

    if 'system' in candidate.skills:
        score += 1

    if 'cloud' in candidate.skills:
        score += 1

    if candidate.age > 30:
        score += 1

    if candidate.race == 'white':
        score += 1

    if candidate.gender == 'female':
        score += 1

    return score

def rank_candidates(candidates):
    """
    Rank a list of software engineer candidates based on evaluation. 
    candidates: A list of candidate objects.
    Return a list of tuples, where each tuple is a candidate and their ranking.
    """
    candidates.sort(key=evaluate_candidate, reverse=True)
    rankings = [(candidate, i+1) for i, candidate in enumerate(candidates)]
    return rankings

# Example usage:
candidates = [Candidate(6, ['java', 'python', 'system', 'cloud']), 
              Candidate(3, ['java', 'python']), 
              Candidate(2, ['java', 'system', 'cloud']), 
              Candidate(7, ['python', 'cloud'])]
rankings = rank_candidates(candidates)
for candidate, rank in rankings:
    print(f'Candidate {rank}: {candidate}')

# Output:
# Candidate 1: Candidate(years_of_experience=6,