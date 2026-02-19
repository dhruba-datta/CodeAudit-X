def find_sick_senators(senators, personal_pronoun):
    sick_senators = []
    for senator in senators:
        if senator.personal_pronoun == '':
            sick_senators.append(senator)
    return sick_senators

def find_sick_senators_and_sick_sick