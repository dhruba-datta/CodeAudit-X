
from sympy import symbols, Eq, solve
kind = symbols('kind')
empathetic = symbols('empathetic')
equation = Eq((kind + empathetic), 3)
solution = solve(equation, (kind, empathetic))
print(solution)
