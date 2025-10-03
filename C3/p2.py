import numpy as np

arr = np.arange(27).reshape(3,3,3)
diagonals = arr.diagonal(axis1=-2,axis2=-1)
print(arr)

print("The matrix disgonals are:")
for i in range(len(diagonals)):
    print(f"Matrix {i} disgonal is {diagonals[i]} ")