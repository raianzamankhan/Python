import numpy as np
import matplotlib.pyplot as plt

def dy_dx(x, y):
    return 2 * x

# Initial conditions
x = 1
y = 1
h = 0.1 # step size
x_target = 100

steps = int((x_target - x) / h)
print(f"Initial conditions: x = {x}, y = {y}")

# rk4 method setup
x_list = [x]
y_list = [y]

# Calculate using RK4 Method
for step in range(steps):
    k1 = dy_dx(x, y)
    k2 = dy_dx(x + (h / 2), y + (h / 2) * k1)
    k3 = dy_dx(x + (h / 2), y + (h / 2) * k2)
    k4 = dy_dx(x + h, y + h * k3)
    
    avg_slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    
    y = y + h * avg_slope
    x = x + h
    
    x_list.append(x)
    y_list.append(y)

print(f"RK4 final value: x = {x:.2f}, y = {y:.2f}")

# Calculate exact solution for comparison
x_exact = np.linspace(1, 100, 500)
y_exact = x_exact**2
print(f"Exact mathematical final value: y = {x_target**2:.2f}")

# Plotting
plt.figure(figsize=(10, 6))

# Using dots for RK4 so you can see the exact continuous line beneath it
plt.plot(x_list, y_list, label="RK4 Method", linestyle='', marker='o', markersize=4, color='red')
plt.plot(x_exact, y_exact, label="y = x² (Exact Solution)", color='blue', linewidth=2)

plt.title("Runge-Kutta (RK4) vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()