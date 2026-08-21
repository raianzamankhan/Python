import numpy as np
import matplotlib.pyplot as plt

# 1. Define x and calculate y values
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 2. First Subplot: sin(x)
# (2 rows, 1 column, 1st panel)
plt.subplot(2, 1, 1)
plt.plot(x, y_sin, color="cyan", linestyle="--", label="sin(x)")
plt.title("Plot 1: sin(x)")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)

# 3. Second Subplot: cos(x)
# (2 rows, 1 column, 2nd panel)
plt.subplot(2, 1, 2)
plt.plot(x, y_cos, color="green", linestyle=":", label="cos(x)")
plt.title("Plot 2: cos(x)")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.legend()
plt.grid(True)

# 4. Automatically adjust spacing so titles/labels don't overlap
plt.tight_layout()

# 5. Display the figure
plt.show()