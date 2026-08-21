import numpy as np
from scipy.optimize import minimize_scalar

# Feed Stream Properties
v0 = 5000 * 0.00378541  # m3/hr
m0 = 1000 * v0  # kg/hr
c0 = 4.2  # kJ/kgK

# Operating Temperatures for Heat Exchanger (K)
TC1, TH1, TH2 = 293.15, 338.15, 303.15  # 293.15 < TC2 < 338.15

# Heat Exchanger Specifications
U, F = 400, 0.8  # W/m2K, dimensionless

# Reactor & Kinetics Parameters
Xa = 0.8  # Fractional conversion
k0, Ea, R = 2.5, 29099, 8.314  # s^-1, J/mol, J/mol.K

# Capital Recovery Factor
i, n = 0.07, 12
CRF = (i * (1 + i) ** n) / ((1 + i) ** n - 1)


def objective(x):
    TC2 = x

    # Heat Exchanger Heat Duty
    Q = m0 * c0 * (TC2 - TC1)  # kJ/hr

    # Log Mean Temperature Difference (LMTD)
    dT1, dT2 = TH1 - TC2, TH2 - TC1
    delTlm = (dT1 - dT2) / np.log(dT1 / dT2)

    # Heat Exchanger Surface Area
    Q_watts = Q * (1000 / 3600)  # W
    Ahx = Q_watts / (U * F * delTlm)  # m^2

    # Utility Cost
    UC = 5e-6 * Q  # dollar/hr
    AUC = UC * 365 * 24  # dollar/year

    # Volume of The Reactor Container
    k = k0 * np.exp(-Ea / (R * TC2))  # s^-1
    V = ((v0 / 3600) * Xa) / (k * (1 - Xa))  # m^3

    # Annualized Capital Cost
    ACC = (17000 * V**0.85 + 12000 * Ahx**0.57) * CRF  # dollar/year

    # Equivalent Annual Operating Cost (Objective Function)
    EAOC = ACC + AUC  # dollar/year
    return EAOC


soln = minimize_scalar(objective, bounds=(TC1 + 0.01, TH1 - 0.01))

print(f"Optimal TC2: {soln.x:.2f} K or {(soln.x - 273.15):.2f} °C")
print(f"Minimum EAOC: ${soln.fun:,.2f} / year")