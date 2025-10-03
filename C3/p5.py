import numpy as np

arr = np.array([
    [1,2],
    [3,4]
])

if np.linalg.det(arr) != 0:
    arr_inv = np.linalg.inv(arr)
    print('Origional matrix: ')
    print(arr)
    print('Inverted Matrix')
    print(arr_inv)
else:
    print('Matrix is not invertible')