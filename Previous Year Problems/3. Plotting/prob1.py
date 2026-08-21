import numpy as np
import matplotlib.pyplot as plt

# --- 1. DATA CREATION ---
# x values from 1 to 50 with an interval of 5
# np.linspace(start, stop, num)  --> 3rd arg = TOTAL NUMBER of points (good for smooth plots)
# np.arange(start, stop, step)   --> 3rd arg = STEP SIZE / interval (good for specific gaps)
x = np.arange(1, 51, 5)

# Mathematical functions
y1 = np.sin(4 * np.pi * x / 180)
y2 = np.log(4 * x + 2)  # np.log is natural log (ln)

# --- 2. SUBPLOT 1: Sine Function ---
plt.subplot(2, 1, 1)  # 2 row, 1 columns, 1st section
plt.plot(x, y1, color='red', marker='x', linestyle='--', label='sine curve')
plt.title('Plot 1: sin(x)')
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()

# --- 3. SUBPLOT 2: Ln Function ---
plt.subplot(2, 1, 2)  # 2 row, 1 columns, 2nd section
plt.plot(x, y2, color='green', marker='s', linestyle='-.', label='ln curve')
plt.title('Plot 2: ln(x)')
plt.xlabel('x values')
plt.ylabel('ln(x)')
plt.grid(True)
plt.legend()

# Prevent overlapping of titles and axis labels
plt.tight_layout()
plt.show()