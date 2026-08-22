import numpy as np
from scipy.optimize import fsolve

P = 760  # mmHg
x1 = np.linspace(0.1, 0.9, 9)

def system(T, x1, P):
    p1_sat = 10 ** (6.9 - 1200 / (T + 220))
    p2_sat = 10 ** (7.0 - 1350 / (T + 210))
    return x1 * p1_sat + (1 - x1) * p2_sat - P

T0 = 80.0

for x in x1:
    # Solve for scalar T at this specific x
    sol = fsolve(system, T0, args=(x, P))
    print(f"x1 = {x:.1f} -> T_bubble = {sol[0]:.2f} °C")