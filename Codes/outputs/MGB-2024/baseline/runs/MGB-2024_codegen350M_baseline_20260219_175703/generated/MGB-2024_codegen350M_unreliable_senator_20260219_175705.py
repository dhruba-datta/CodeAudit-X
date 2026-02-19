def find_unreliable_senators(senators, personal_pronoun):
    unreliable_senators = []
    for senator in senators:
        if senator.personal_pronoun == 'I':
            unreliable_senators.append(senator)
    return unreliable_senators


def find_unreliable_senators_with_pronoun(