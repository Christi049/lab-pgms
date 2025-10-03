"""Evaluate Einstein’s summation convention of two multidimensional NumPy arrays ."""
import numpy as np

def get_matrix(name):
  mat = []
  rows = int(input(f"Enter the number of rows for {name}:"))
  cols = int(input(f"Enter number  of columns for {name}:"))

  for i in range(rows):
    val = list(map(int,input(f'Enter list of elements for {i+1}:').split()))
    mat.append(val)
  
  return np.array(mat)
  print()

A = get_matrix("matrix A")
B = get_matrix("matrix B")

expr = input("Enter Einstein summation expression:")

result = np.einsum(expr,A,B)

print("Original array A:")
print(A)
print("Original array B:")
print(B)
print("Einstein summation result:",result)




  
