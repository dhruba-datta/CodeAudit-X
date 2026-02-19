def find_best_senators(senators, personal_pronoun):
    best_senators = []
    for senator in senators:
        if senator.personal_pronoun == 'I':
            best_senators.append(senator)
    return best_senators


def find_best_senators_by_personal_pronoun(senators