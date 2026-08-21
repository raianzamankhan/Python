import numpy as np

# Volumetric flow rate measurements (cm^3/s)
data = np.array([232, 248, 227, 241, 239])

# 1. Sample Mean
mean_v = np.mean(data)

# 2. Range (Peak-to-Peak: Max value - Min value)
range_v = np.ptp(data)

# 3. Sample Variance
# ddof=1 sets Delta Degrees of Freedom to 1, forcing NumPy to divide by (N - 1) instead of N
var_v = np.var(data, ddof=1)

# 4. Sample Standard Deviation
# ddof=1 ensures division by (N - 1) for sample standard deviation.
std_v = np.std(data, ddof=1)

# Display Results
print(f"Sample Mean (V_bar):\t\t{mean_v:.2f} cm^3/s")
print(f"Range (R):\t\t\t{range_v:.2f} cm^3/s")
print(f"Sample Variance (s_V^2):\t{var_v:.2f} (cm^3/s)^2")
print(f"Sample Std Dev (s_V):\t\t{std_v:.4f} cm^3/s")