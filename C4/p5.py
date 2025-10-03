"""Compute the eigenvalues and eigenvectors of a given
square matrix using NumPy"""
import numpy as np

n = int(input("Enter the no. of rows and columns:"))
print("Enter matrix elements row by row")
matrix_elements = []

for i in range(n):
    row = list(map(int,input(f"Enter elemenst of row {i+1} :").split()))
    matrix_elements.append(row)

matrix_np = np.array(matrix_elements)
eigenValues, eigenVectors = np.linalg.eig(matrix_np)

print("Original matrix:")
print(matrix_np)
print("Eigen values:")
print(eigenValues)
print("Eigen vectors:")
print(eigenVectors)