import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
maths= np.array([20,18,14,15,16])
student=np.array(["ubaid","burhan","wahid","zahim","hazik"])

figures , axes= plt.subplots(2,2)

axes[0,0].bar(x,maths,color="red", label="math_marks")
axes[0,0].set_title("math_marks")

axes[0,1].pie(x,labels=student,autopct="%1.1f%%",radius=1.3, startangle=90)
axes[0,1].set_title("x**2")

axes[1,0].plot(x,x**3,color="green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**4,color="purple")
axes[1,1].set_title("x**4")

plt.tight_layout()

plt.show()