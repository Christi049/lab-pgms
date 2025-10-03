"""Compute pearson product-moment correlation coefficients of two given NumPy arrays"""

import numpy as np

x = np.array(list(map(int,input('Enter elements of first array:').split())))
y = np.array(list(map(int,input('Enter elements of second array:').split())))

if len(x) != len(y):
  print("Lenght of both arrays must be same")

corr_matrix = np.corrcoef(x,y)

print("Correlation matrix:",corr_matrix)
print("Pearson correlation coeficients:",corr_matrix[0,1])

