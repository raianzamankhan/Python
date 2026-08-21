from scipy.optimize import minimize

def f(vars):
    x, y = vars
    return x**2 + y**2 + 4 * x - 6 * y

initial_guess = [0, 0]
res_min = minimize(f, initial_guess, bounds=[(-5, 5), (-5, 5)])
# Note: 'bounds' is not strictly necessary for res_min because f(x, y) has a true global minimum at (-2, 3).
print(f"Minimum: x = {res_min.x[0]:.4f}, y = {res_min.x[1]:.4f}, f(x, y) = {res_min.fun:.4f}")