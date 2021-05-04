from cogs.Math import derivate_main
import sympy as sp

def derivate(a, b, c):
    x = sp.Symbol("x")
    return str(sp.diff(a*x**2 + b*x + c))
x = derivate(1, 2, 1)
print(str(x))