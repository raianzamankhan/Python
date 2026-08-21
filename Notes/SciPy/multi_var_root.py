from scipy.optimize import fsolve

# 1. Linear System:
#    2x + y = 5  ->  2x + y - 5 = 0
#    x - y = 1   ->  x - y - 1 = 0
def linear_system(vars):
    x, y = vars
    eq1 = 2 * x + y - 5
    eq2 = x - y - 1
    return [eq1, eq2]

# 2. Non-linear System:
#    x^2 + y^2 = 25  ->  x^2 + y^2 - 25 = 0
#    x * y = 12      ->  x * y - 12 = 0
def nonlinear_system(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 25
    eq2 = x * y - 12
    return [eq1, eq2]

# Solve Linear System
initial_guess = [0, 0]
res_linear = fsolve(linear_system, initial_guess)
print(f"Linear System Roots: x = {res_linear[0]:.4f}, y = {res_linear[1]:.4f}")

# Solve Non-linear System
initial_guess = [1, 2]
res_nonlinear = fsolve(nonlinear_system, initial_guess)
print(f"Non-linear Positive Roots: x = {res_nonlinear[0]:.4f}, y = {res_nonlinear[1]:.4f}")

# Note: The :.4f format modifier is important because numerical solvers stop within a tiny tolerance,
# which can leave slight floating-point artifacts (e.g., 2.9999999999999996 instead of 3.0).
# Formatting cleans up the display to the desired decimal precision.