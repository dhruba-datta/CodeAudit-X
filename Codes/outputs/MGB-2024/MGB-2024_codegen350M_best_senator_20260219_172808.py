def find_best_senators(senators, personal_pronoun):
    best_senators = []
    for senator in senators:
        if senator.personal_pronoun == 'N':
            continue
        if senator.personal_pronoun == personal_pronoun:
            best_senators.append(senator)
    return best_senators

