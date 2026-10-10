import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008])

x = np.array([2, 4, 5, 6, 7, 8, 23, 45, 32])

age = np.array([14, 15, 16, 17, 18, 19, 20, 21, 22])

plt.plot(years, x, color="blue", marker="o", label="Values")
plt.plot(years, age, color="red", marker="*", label="Age")

plt.title("Values Over the Years")
plt.xlabel("Years")
plt.ylabel("Values")

plt.xticks(years)
plt.grid(True)
plt.legend()

plt.show()