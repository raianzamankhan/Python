import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y, z = vars

    eq1 = x + y + z - 3
    eq2 = np.exp(x) + y**2 - 4
    eq3 = np.sin(z) + x - 1

    return [eq1, eq2, eq3]

initial_guess = [1, 1, 1]

x, y, z = fsolve(equations, initial_guess)

print("--- Solution ---")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")
print(f"z = {z:.4f}")