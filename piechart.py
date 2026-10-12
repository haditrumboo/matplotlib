import matplotlib.pyplot as plt
import numpy as np

expenses = np.array(["Food", "Rent", "Travel", "Shopping", "Bills", "Savings"])

amount = np.array([4000, 10000, 2000, 3000, 1500, 5000])
plt.pie(amount, labels=expenses, autopct="%1.1f%%", explode=[0,0.1,0,0,0,0],shadow=True, startangle=90)
plt.axis("equal")
plt.legend(expenses, title="Expense Categories", loc="best")
plt.show()