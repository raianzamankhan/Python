from scipy.optimize import minimize

# Target function: f(x, y) = x^2 + y^2 + 4x - 6y = (x + 2)^2 + (y - 3)^2 - 13
# Analytical extrema: Global minimum at (-2, 3) with f(-2, 3) = -13
def f(vars):
    x, y = vars
    return x**2 + y**2 + 4 * x - 6 * y

# Minimizing -f(x, y) is mathematically equivalent to maximizing f(x, y)
def neg_f(vars):
    return -f(vars)

# 1. Find Minimum
initial_guess = [0, 0]
res_min = minimize(f, initial_guess)
# Note: 'bounds' is not strictly necessary for res_min because f(x, y) has a true global minimum at (-2, 3).
print(f"Minimum: x = {res_min.x[0]:.4f}, y = {res_min.x[1]:.4f}, f(x, y) = {res_min.fun:.4f}")

# 2. Find Maximum (within bounds)
initial_guess = [0, 0]
res_max = minimize(neg_f, initial_guess, bounds=[(-5, 5), (-5, 5)])
print(f"Maximum: x = {res_max.x[0]:.4f}, y = {res_max.x[1]:.4f}, f(x, y) = {-res_max.fun:.4f}")

# Notes:
# 1. 'minimize' requires an initial guess [x0, y0] and passes variables as an array.
# 2. 'bounds' takes a list of intervals [(min_x, max_x), (min_y, max_y)] for each variable.
# 3. 'res.x' stores the solution array (res.x[0] for x, res.x[1] for y), while 'res.fun' holds the function value at that point.
# 4. '-res_max.fun' negates the result back to obtain the true maximum value.
# 5. Because this surface opens upward infinitely, the maximum lies on the search boundary at (5, -5).
# 6. ':.4f' formats the float output to clear minor numerical solver precision noise.