"""Convert a NumPy array into a csv file"""
import numpy as np

arr = np.array([
    [1,2],
    [3,4],
    [5,6]
])

np.savetxt("cstat.csv", arr, delimiter=',', fmt="%d")

