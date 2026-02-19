def find_reliable_senators(senators, personal_pronoun):
    reliable_senators = []
    for senator in senators:
        if senator.personal_pronoun == 'I' and senator.pronoun == personal_pronoun:
            reliable_senators.append(senator)
    return reliable_senators


def find_reliable