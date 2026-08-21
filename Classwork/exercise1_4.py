import numpy as np
import matplotlib.pyplot as plt

# 1. Define x values (e.g., from 0 to 2*pi)
x = np.linspace(0, 2 * np.pi, 100)
# print(x)

# 2. Calculate y values for sin(x) and cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 3. Plot both curves & assign labels (these labels supply the text for plt.legend below)
plt.plot(x, y_sin, label="sin(x)", color="cyan", linestyle="--")
plt.plot(x, y_cos, label="cos(x)", color="green", linestyle=":")

# Draw reference axes crossing at (0,0)
plt.axhline(color="black")  # Horizontal reference line along y = 0
plt.axvline(color="black")  # Vertical reference line along x = 0

# Replace numeric x-axis ticks with custom pi-formatted text labels
plt.xticks(
    [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],  # Exact numerical tick positions
    ["0", "π/2", "π", "3π/2", "2π"]                   # Text labels to display at those positions
)

# 4. Add title, labels, legend, and grid
plt.title("Plot of sin(x) and cos(x)")
plt.xlabel("x")
plt.ylabel("sin(x) and cos(x)")

# Reads the 'label' strings defined above and displays them in the plot key/box
plt.legend()
plt.grid(True)

# 5. Display the figure
plt.show()