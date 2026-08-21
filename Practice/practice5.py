import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def rate(Ca, k, n):
    return (k*Ca**n)

Ca = np.array([0.2,0.3,0.4,0.5,0.6])
r_exp = np.array([4.472,5.477,6.325,7.071,7.746])/10

popt, pcov = curve_fit(rate, Ca, r_exp, p0=[1,1])

print(f"The estimated rate constant k = {popt[0]:.2f}")
print(f"The order of the reaction n = {popt[1]:.2f}")

plt.scatter(Ca, r_exp, color="red", label="r_exp")
plt.plot(Ca,rate(Ca,popt[0],popt[1]), label="fitted curve")
plt.xlabel("Concentration")
plt.ylabel("Rate of reaction")
plt.legend()
plt.grid()
plt.show()