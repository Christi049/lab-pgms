import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
a_flatten = a.flatten()
a_list = a_flatten.tolist()

print("Original matrix:",a)
print("Converted array:",a_list)
