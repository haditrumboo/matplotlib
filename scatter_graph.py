import matplotlib.pyplot as plt
import numpy as np

students = np.array(["Hadi", "Sahil", "Burhan", "Ayesha", "Sara",
"Omar", "Zoya", "Adil", "Mehak", "Danish"])

study_hours = np.array([1, 2, 3, 4, 5, 6, 2, 7, 8, 4])
marks = np.array([35, 40, 50, 60, 75, 85, 45, 90, 95, 65])

plt.scatter(study_hours, marks, c=marks, cmap="viridis", s=100)

for i in range(len(students)):
    plt.annotate(students[i], (study_hours[i], marks[i]))

plt.title("Study Hours vs Exam Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.colorbar(label="Marks")
plt.grid()

plt.show()
