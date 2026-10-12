import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024])
sales = np.array([100, 150, 120, 200, 250])
expenses = np.array([80, 90, 100, 130, 160])

plt.plot(years,sales,color="green",marker="o",label="Annual sales")
plt.plot(years,expenses,color="red", marker="o", label="expenses")
plt.xticks(years,color="skyblue")
plt.yticks(color="skyblue")
plt.title('sales vs expenses', fontsize=20, family="arial")
plt.xlabel("year")
plt.ylabel("amount")
plt.grid(axis="y",linestyle="dashed")
plt.legend()
plt.show()