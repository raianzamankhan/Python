import numpy as np

# Given constants
K_0 = 350  # W/cm
T_0 = 68   # K

print(f"Temperature (T)\t| Conductivity (K)")
print("-" * 35)

for T in range(200, 701, 50):
    # Calculates thermal conductivity K(T) = K_0 / (T - T_0)
    K = K_0 / (T - T_0)
    print(f"{T}\t\t| {K:.4f}")
print("-" * 35)