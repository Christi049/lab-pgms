"""NumPy – Fibonacci Series using Binet Formula"""

import numpy as np

s5 = np.sqrt(5)
k = np.arange(10)
phi = (1+s5)/2
psi = (1-s5)/2

fib = (phi**k - psi**k)/s5

print("Fibonacci series:")
print(np.round(fib).astype(int))

