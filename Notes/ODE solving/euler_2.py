import numpy as np
import matplotlib.pyplot as plt

def dy_dx(x, y):
    return 2 * x

# Initial conditions
x = 1
y = 1
h = 0.1 # Step size
x_target = 100

steps = int((x_target - x) / h)
print(f"Initial conditions: x = {x}, y = {y}")

# Euler's method setup
x_list = [x]
y_list = [y]

# Calculate using Euler's Method
for step in range(steps):
    slope = dy_dx(x, y)
    y = y + h * slope
    x = x + h
    x_list.append(x)
    y_list.append(y)

print(f"Euler's method final value: x = {x:.2f}, y = {y:.2f}")

# Calculate the exact solution (y = x^2) for comparison
# Note: C=0 because y(1) = 1^2 + C => 1 = 1 + C => C = 0
x_exact = np.linspace(1, 100, 500)
y_exact = x_exact**2
print(f"Exact mathematical final value: y = {x_target**2:.2f}")

# Plotting both curves
plt.figure(figsize=(10, 6))
plt.plot(x_list, y_list, label="Euler's Method (Approximation)", linestyle='--', color='red')
plt.plot(x_exact, y_exact, label="y = x² (Exact Solution)", color='blue', alpha=0.6)

plt.title("Euler's Method vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()