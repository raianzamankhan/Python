from scipy.optimize import fsolve

# 1. Linear Equation: 3x - 12 = 0
def linear_eq(x):
    return 3 * x - 12

# 2. Non-linear Equation: x^2 - 5 = 0
def nonlinear_eq(x):
    return x**2 - 5

# Solve Linear Equation
initial_guess = 0.0
res_linear = fsolve(linear_eq, initial_guess)
print("Linear Root:", res_linear[0])

# Solve Non-linear Equation
initial_guess = 1.0
res_nonlinear = fsolve(nonlinear_eq, initial_guess)
print("Non-linear Positive Root:", res_nonlinear[0])