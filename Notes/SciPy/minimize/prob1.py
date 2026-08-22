from scipy.optimize import minimize

def objt(vars):
    x, y = vars
    return 100 * (y - x**2)**2 + (1 - x)**2

initial_guess = [0, 0]
soln = minimize(objt, initial_guess, bounds=([-2, 2], [-1, 3]))

print(f"Optimal x: {soln.x[0]:.4f}")
print(f"Optimal y: {soln.x[1]:.4f}")
print(f"Minimum function value: {soln.fun:.4e}")