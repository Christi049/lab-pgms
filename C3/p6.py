"""Calculate inner, outer, and cross products of matrices and vectors using NumPy

"""
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
inner_vec = np.inner(a,b)
outer_vec = np.outer(a,b)
cross_vec = np.cross(a,b)

print("VECTOR CALCULATIONS")
print("Inner product:",inner_vec)
print("Outer product:",outer_vec)
print("Cross product:",cross_vec)

A = np.array([
    [1,2],
    [3,4]
])
B = np.array([
    [5,6],
    [7,8]
])
inner_mat = np.inner(A,B)
outer_mat = np.outer(A,B)
cross_mat = np.cross(A,B)

print("MATRIX CALCULATIONS")
print("Inner product:",inner_mat)
print("Outer product:",outer_mat)
print("Cross product:",cross_mat)