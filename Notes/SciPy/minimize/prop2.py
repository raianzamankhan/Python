import numpy as np
from scipy.optimize import minimize

# 1. Objective function: Surface area A = 2*pi*r^2 + 2*pi*r*h
def area(vars):
    r, h = vars
    return 2 * np.pi * r**2 + 2 * np.pi * r * h

# 2. Constraint function: pi*r^2*h - 50 = 0
def volume_constraint(vars):
    r, h = vars
    return np.pi * (r**2) * h - 50.0

# Initial guess and bounds
initial_guess = [2.0, 5.0]
bounds = [(0.1, None), (0.1, None)]  # r >= 0.1, h >= 0.1

# Define the equality constraint dictionary
cons = {'type': 'eq', 'fun': volume_constraint}

# 3. Solve using SLSQP
soln = minimize(area, initial_guess, method='SLSQP', bounds=bounds, constraints=cons)

# 4. Display results
print(f"Optimal Radius (r) : {soln.x[0]:.4f} m")
print(f"Optimal Height (h) : {soln.x[1]:.4f} m")
print(f"Minimum Surface Area: {soln.fun:.4f} m^2")