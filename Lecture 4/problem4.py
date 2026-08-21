import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# =========================================
# 1. MODEL FUNCTIONS (The Blueprint / Shape)
# =========================================
# Tells curve_fit which mathematical shape to bend and fit through the data points:
#
# 1. Straight Line: y = m*x + c
#    m = slope (steepness), c = y-intercept
#
# 2. Parabola: y = a*x**2 + b*x + c
#    a = curvature (width/direction), b = tilt/shift, c = y-intercept
#
# 3. Exponential: y = a*np.exp(-b*x) + c
#    a = initial amplitude (height), b = decay rate (speed), c = baseline offset (floor)


def exp_decay(x, a, b, c):
  return a * np.exp(-b * x) + c


# =========================================
# 2. GENERATING BENCHMARK DATA
# =========================================
x = np.linspace(0, 4, 50)

a_true, b_true, c_true = 2.5, 1.3, 0.5
y_true = exp_decay(x, a_true, b_true, c_true)  # Suppose this is the true data to generate an experimental data around it

noise = np.random.normal(0, 0.2, size=x.size)
y_exp = y_true + noise  # This is what an experimental data would look like

# =========================================
# 3. CURVE_FIT INPUTS & OUTPUTS
# =========================================
# Inputs:
# - exp_decay : The equation formula/shape to fit.
# - x         : Horizontal data points.
# - y_exp     : Measured noisy data points (vertical values).
# - p0        : "Parameters at step 0" -> Initial starting guess for [a, b, c].
#
# Outputs:
# - popt : "Parameters Optimized" -> The winning [a, b, c] values that fit the dots best.
# - pcov : "Parameter Covariance" -> A 3x3 matrix measuring uncertainty in those values.

popt, pcov = curve_fit(exp_decay, x, y_exp, p0=[1, 1, 1])

# =========================================
# 4. WHAT IS PCOV (The 3x3 Matrix)
# =========================================
# Size is 3x3 because we have 3 unknown parameters (a, b, c).
#
# - Diagonal (3 values):
#   Individual variance (uncertainty^2) for each parameter: [Var(a), Var(b), Var(c)].
#
# - Off-diagonal (6 values):
#   Covariance -> How turning one knob forces another knob to move to keep the fit.

# =========================================
# 5. EXTRACTING THE ERROR (± Margin)
# =========================================
# - perr          : "Parameter Errors" -> 1D array of ± uncertainties [error_a, error_b, error_c].
# - np.diag(pcov) : Grabs the 3 diagonal variance values (sigma^2).
# - np.sqrt(...)  : Takes the square root because variance is in squared units (meters^2).
#                   Square root brings it back to regular units (meters) so they match.
#
# What error means:
# If a = 2.50 and error = 0.05, the result is: a = 2.50 ± 0.05
# (Not a mistake/bug, but the statistical wiggle room due to noisy data).

perr = np.sqrt(np.diag(pcov))

# =========================================
# 6. R-SQUARED (Goodness of Fit)
# =========================================
# Formula: R² = 1 - Σ(y_data - y_fit)² / Σ(y_data - y_mean)²
# Closer to 1.0 = better fit
r2 = 1 - np.sum((y_exp - exp_decay(x, *popt))**2) / np.sum((y_exp - np.mean(y_exp))**2)

# =========================================
# 7. RESULTS & PLOT
# =========================================
print(f"a = {popt[0]:.3f} ± {perr[0]:.3f} (True: {a_true})")
print(f"b = {popt[1]:.3f} ± {perr[1]:.3f} (True: {b_true})")
print(f"c = {popt[2]:.3f} ± {perr[2]:.3f} (True: {c_true})")

# 1. Plot noisy experimental measurements as individual dots
plt.scatter(x, y_exp, color="red", label="Experimental Data", s=15)

# 2. Plot the smooth fitted curve
plt.plot(x, exp_decay(x, *popt), color="blue", label=f"Fitted Model (R² = {r2:.4f})", linestyle="-", linewidth=2)

# 3. Plot the true/ideal underlying curve
plt.plot(x, y_true, color="green", label="True Data", linestyle=":", linewidth=1.5)

plt.title("Exponential Decay Curve Fitting")
plt.xlabel("Time")
plt.ylabel("Signal")
plt.grid(linestyle="--", alpha=0.5)
plt.legend()
plt.show()