import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Physical Constants
rho_s = 1800.0        # kg/m^3
rho = 1000.0          # kg/m^3
a = 30.0 * 9.8        # m/s^2 (294 m/s^2)
mu = 0.01             # Pa.s

Dp_array = np.arange(0.2, 0.301, 0.01) * 1e-3  # m

def system(vars, Dp):
    Vt, Cd, Re = vars
    
    # Drag coefficient relation
    if Re < 1.0:
        Cd_calc = 24.0 / Re
    elif Re <= 1000.0:
        Cd_calc = (24.0 / Re) * (1.0 + 0.14 * (Re**0.7))
    else:
        Cd_calc = 0.44
        
    # Residual equations (f(vars) = 0)
    eq1 = Vt - np.sqrt((4.0 * (rho_s - rho) * a * Dp) / (3.0 * Cd * rho))
    eq2 = Cd - Cd_calc
    eq3 = Re - (Dp * rho * Vt) / mu
    
    return [eq1, eq2, eq3]

# Solve for each diameter
Vt_list = []
guess = [1.0, 24.0, 1.0]  # Initial guess [Vt, Cd, Re]

for Dp in Dp_array:
    sol = fsolve(system, guess, args=(Dp,))
    Vt_list.append(sol[0])
    guess = sol  # Use current solution as the next guess for speed/stability

Vt_list = np.array(Vt_list)

# Plotting
plt.plot(Dp_array * 1e3, Vt_list, marker='o', color='crimson')
plt.title("Terminal Velocity vs. Coal Particle Diameter (fsolve)")
plt.xlabel("Particle Diameter, $D_p$ (mm)")
plt.ylabel("Terminal Velocity, $V_t$ (m/s)")
plt.grid(True)
plt.show()