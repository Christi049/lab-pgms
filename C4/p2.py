"""Calculate the average, variance and standard deviation in Python using NumPy 

"""
import numpy as np

arr = list(map(int,input("Enter list of elements in array:").split()))

arr_np = np.array(arr)
mean = np.mean(arr_np)
var = np.var(arr_np)
std = np.std(arr_np)

print(f"Mean is :{mean}")
print(f"Mean is :{var}")
print(f"Mean is :{std}")