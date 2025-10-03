import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = np.sin(x)  

plt.plot(x, y)
plt.title("Plot of y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
