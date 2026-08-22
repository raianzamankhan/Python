import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Tsample = np.array([
    0.0, 3.8, 8.0, 13.0, 18.2, 20.0, 27.8, 33.1, 37.6, 43.0, 47.7,
    51.2, 52.1, 63.3, 68.4, 73.4, 78.4, 83.4, 90.4, 93.4, 98.7
]) # x value

Tstandard = np.array([
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
    55, 60, 65, 70, 75, 80, 85, 90, 95, 100
]) # y value

def linear(Tsample, m, c):
    return (m*Tsample+c)
def quadratic(Tsample,a,b,c):
    return (a*Tsample**2+b*Tsample+c)
def cubic(Tsample,a,b,c,d):
    return (a*Tsample**3+b*Tsample**2+c*Tsample+d)

popt_lin, _ = curve_fit(linear, Tsample, Tstandard, p0=[1,1])
popt_quad, _ = curve_fit(quadratic, Tsample, Tstandard, p0=[1,1,1])
popt_cub, _ = curve_fit(cubic, Tsample, Tstandard, p0=[1,1,1,1])

r2_lin = 1 - np.sum((Tstandard-linear(Tsample, *popt_lin))**2)/np.sum((Tstandard-np.mean(Tstandard))**2)
r2_quad = 1 - np.sum((Tstandard-quadratic(Tsample, *popt_quad))**2)/np.sum((Tstandard-np.mean(Tstandard))**2)
r2_cub = 1 - np.sum((Tstandard-cubic(Tsample, *popt_cub))**2)/np.sum((Tstandard-np.mean(Tstandard))**2)

print(f"Linear prediction at 80°C:    {linear(80, *popt_lin):.2f}°C")
print(f"Quadratic prediction at 80°C: {quadratic(80, *popt_quad):.2f}°C")
print(f"Cubic prediction at 80°C:     {cubic(80, *popt_cub):.2f}°C")

models = ["Linear", "Quadratic", "Cubic"]
r2_values = [r2_lin, r2_quad, r2_cub]

best_idx = r2_values.index(max(r2_values))

print(f"Best fitting model: {models[best_idx]} with R² = {r2_values[best_idx]:.6f}")

plt.scatter(Tsample, Tstandard, color="red", s=15, label="Experimental Data")
plt.plot(Tsample, linear(Tsample, *popt_lin), color="blue", linestyle="-", label=f"Linear (R² = {r2_lin:.4f})")
plt.plot(Tsample, quadratic(Tsample, *popt_quad), color="green", linestyle="--", label=f"Quadratic (R² = {r2_quad:.4f})")
plt.plot(Tsample, cubic(Tsample, *popt_cub), color="purple", linestyle=":", label=f"Cubic (R² = {r2_cub:.4f})")

plt.xlabel("Sample Thermometer Reading (°C)")
plt.ylabel("Standard Thermometer Reading (°C)")
plt.legend()
plt.grid()
plt.show()