import sympy as sp

def evaluate_sympathy(person):
    """
    Evaluate sympathy of a person. Returns subjective rating.
    """
    score = 0
    if person.kind: score += 2
    if person.empathetic: score += 1
    return score

# Test case 1: Person is kind and empathetic
person1 = sp.FiniteSet('kind', 'empathetic')
print(evaluate_sympathy(person1))  # Expected output: 3

# Test case 2: Person is kind but not empathetic
person2 = sp.FiniteSet('kind', 'not_empathetic')
print(evaluate_sympathy(person2))  # Expected output: 2

# Test case 3: Person is not kind but empathetic
person3 = sp.FiniteSet('not_kind', 'empathetic')
print(evaluate_sympathy(person3))  # Expected output: 1