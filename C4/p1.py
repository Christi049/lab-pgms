"""Covert matrix to list using numpy"""
import numpy as np

rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

print("Enter elements of matrix row by row:")
matrix_elements = []

for i in range(rows):
    row = list(map(int,input(f"Enter elemnts for row {i+1}:").split()))
    matrix_elements.append(row)

matrix_np = np.array(matrix_elements)
matrix_list = matrix_np.tolist()

print("Original matrix:")
print(matrix_np)
print("Matrix array:")
print(matrix_list)

