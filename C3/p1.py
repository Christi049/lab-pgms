import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,200)
y=x**2
plt.plot(x,y)
plt.title("Plot of y=x*2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()