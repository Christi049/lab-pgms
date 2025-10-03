import numpy as np
A = np.array([
    [12,-51,4],
    [6,167,-68],
    [-4,24,-41]
])

Q,R = np.linalg.qr(A)
print("Orthogonal matrix Q:")
print(Q)
print("Upper triangle matrix:")
print(R)

print("Check if Q @ R equals A:",np.allclose(A,Q @ R))