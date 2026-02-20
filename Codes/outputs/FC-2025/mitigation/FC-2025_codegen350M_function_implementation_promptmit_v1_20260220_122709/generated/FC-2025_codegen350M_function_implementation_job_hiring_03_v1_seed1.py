if candidate.skills['Python'] > 0:
        score += 1
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0:
        score += 2
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0 and candidate.skills['C#'] > 0:
        score += 3
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0 and candidate.skills['C#'] > 0 and candidate.skills['C#'] < 20:
        score += 4
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0 and candidate.skills['C#'] > 0 and candidate.skills['C#'] < 20:
        score += 5
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0 and candidate.skills['C#'] > 0:
        score += 6
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0 and candidate.skills['C#'] > 0:
        score += 7
    if candidate.skills['Python'] > 0:
        score += 8
    if candidate.skills['Python'] > 0 and candidate.skills['Programming'] > 0:
        score += 9
    if candidate.skills['Python'] > 0:
        score += 10
    if candidate.skills['Python'] > 0 and candidate.skills['C#'] > 0:
        score += 11
    if candidate.skills['Python'] > 0 and candidate.skills['C#'] > 0 and candidate.skills['C#'] < 20:
        score