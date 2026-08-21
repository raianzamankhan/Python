import matplotlib.pyplot as plt
import numpy as np

# Scores per over (1 to 10)
bd_scores = [10, 5, 14, 16, 18, 2, 6, 11, 14, 13]
pak_scores = [7, 16, 3, 5, 7, 15, 10, 12, 17, 18]

overs = np.arange(1, 11)  # Overs 1 to 10
width = 0.35              # Width of each bar

# Plot bars side by side
plt.bar(overs - width/2, bd_scores, width=width, label='Bangladesh')
plt.bar(overs + width/2, pak_scores, width=width, label='Pakistan')

# Labels and legend
plt.xlabel('Over')
plt.ylabel('Runs')
plt.title('Bangladesh vs Pakistan - Score per Over')
plt.xticks(overs)
plt.legend()

plt.show()