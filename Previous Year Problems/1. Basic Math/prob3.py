import numpy as np

# Given constants
mu_0 = 2.414e-5
E = 247.7 * 1000  # Convert kJ/mol to J/mol
R = 8.314

print(f"Temperature (T)\t| Viscosity (mu)")
print("-" * 32)

for T in range(100,1001,50):
    mu = mu_0 * np.exp(E / (R * T))
    print(f"{T}\t\t| {mu:.2e}")
print("-" * 32)