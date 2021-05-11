import sympy as sp

def derivate_main(a, b, c):
    x = sp.Symbol("x")
    return f"{sp.diff(a*x**2 + b*x + c)}"

print(f"{derivate_main(1, 2, 1)}")