import matplotlib.pyplot as plt
import numpy as np

students = np.array(["Hadi", "Sahil", "Burhan", "Ayesha", "Sara"])

python_marks = np.array([85, 70, 90, 65, 80])
sql_marks = np.array([75, 85, 80, 90, 70])
ml_marks = np.array([90, 75, 85, 80, 95])


x = np.arange(len(students))


width = 0.25


plt.bar(x - width, python_marks, width=width, color="green", label="Python")
plt.bar(x, sql_marks, width=width, color="blue", label="SQL")
plt.bar(x + width, ml_marks, width=width, color="orange", label="ML")


plt.xticks(x, students)


plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")


plt.legend()


plt.grid(axis="y", linestyle="--", alpha=0.5)


plt.show()
