def find_reliable_senators(senators, personal_pronoun):
    reliable_senators = []
    for senator in senators:
        if senator.personal_pronoun == 'N':
            continue
        if senator.personal_pronoun == personal_pronoun:
            reliable_senators.append(senator)
    return reliable_senators