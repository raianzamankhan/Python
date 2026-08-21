from scipy.optimize import minimize_scalar

# Target function: f(x) = x^3 - 6x^2 + 9x + 1
# Analytical extrema: Local maximum at (1, 5), Local minimum at (3, 1)
# Note on minimums: Both x=0 (boundary) and x=3 (local valley) evaluate to y=1; 
# the solver converges to x=3 because it actively tracks the concave turning point (f'(x) = 0).
def f(x):
    return x**3 - 6 * x**2 + 9 * x + 1

# Minimizing -f(x) is mathematically equivalent to maximizing f(x)
def neg_f(x):
    return -f(x)

# 1. Find Local Minimum
res_min = minimize_scalar(f, bounds=(0, 5))
print(f"Local Minimum: x = {res_min.x:.4f}, y = {res_min.fun:.4f}")

# 2. Find Local Maximum
res_max = minimize_scalar(neg_f, bounds=(0, 5))
print(f"Local Maximum: x = {res_max.x:.4f}, y = {-res_max.fun:.4f}")

# Notes:
# 1. 'bounds' defines the search range and automatically selects the bounded method.
# 2. '-res_max.fun' negates the result back since minimizing -f(x) yields a negative value at the peak.
# 3. ':.4f' formats the float output to clear minor numerical solver precision noise.
# 4. Although f(0) = f(3) = 1, the algorithm isolates x=3 as the true interior local minimum where slope is zero.