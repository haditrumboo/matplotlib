import matplotlib.pyplot as plt
import numpy as np

scores1 = np.array([78, 79, 80, 81, 82])
scores2 = np.array([60, 70, 80, 90, 100])

plt.subplot(1, 2, 1)
plt.hist(scores1, bins=5, color="lightgreen", edgecolor="black")
plt.title("Small Spread")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(scores2, bins=5, color="orange", edgecolor="black")
plt.title("Large Spread")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()