"""Compute the Kronecker product of two multidimensional NumPy arrays"""
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[0,3],[6,7]])
k = np.kron(a,b)

print("Matrix a:",a)
print("matrix b:",b)
print("Kronecker product:",k)