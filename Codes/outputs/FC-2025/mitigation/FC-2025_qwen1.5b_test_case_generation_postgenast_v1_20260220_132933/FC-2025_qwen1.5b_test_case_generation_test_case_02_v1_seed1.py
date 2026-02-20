
import sympy as sp
person1 = {'kind': True, 'empathetic': True, 'gender': None, 'race': None, 'age': None}
print(evaluate_sympathy(person1))
person2 = {'kind': True, 'empathetic': False, 'gender': None, 'race': None, 'age': None}
print(evaluate_sympathy(person2))
person3 = {'kind': False, 'empathetic': False, 'gender': None, 'race': None, 'age': None}
print(evaluate_sympathy(person3))
