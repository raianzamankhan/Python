import numpy as np
import matplotlib.pyplot as plt

# --- 1. DATA CREATION ---
# x from 1 to 100 with step 0.5
x = np.arange(1, 100.5, 0.5)
y = np.exp(x)

# --- 2. TOP PANEL: Log-Log Plot ---
plt.subplot(2, 1, 1)
plt.loglog(x, y, color='blue', label='y = e^x')
plt.title('Log-Log Plot')
plt.xlabel('x (log scale)')
plt.ylabel('y (log scale)')
plt.grid(True)
plt.legend()

# --- 3. BOTTOM PANEL: Semi-Log Scale for y ---
plt.subplot(2, 1, 2)
plt.semilogy(x, y, color='violet', label='y = e^x')
plt.title('Semi-Log Plot (y-axis log scale)')
plt.xlabel('x (linear scale)')
plt.ylabel('y (log scale)')
plt.grid(True)
plt.legend()

# Display plots
plt.tight_layout()
plt.show()