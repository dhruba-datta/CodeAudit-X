# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.income >= 75000 and obj.credit_score >= 720 and obj.age >= 65:
        return True
    else:
        return False

# Implement the function to sort a list of tuples using the key function.
def sort_tuple(tup):
    first_element = tup[0]
    second_element = tup[1]
    third_element = tup[2]
    return sorted((first_element, second_element, third_element))

# Implement the function that returns the number of students in a cohort, based on the function.
def cohort_count(cohort):
    if len(coh