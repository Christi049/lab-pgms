"""PLot the line graph from NumPy array"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4])
y = np.arange(len(x))

plt.plot(x,y, marker = 'o', linestyle='-')
plt.title("Linear graph")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

