"""Calculate the n-th order discrete difference along the given axis"""
import numpy as np

arr = list(map(int,input("Enter a list of elements:").split()))
arr_np = np.array(arr)

n = int(input("Enter the n-th order discrete distance :"))

diff = np.diff(arr,n=n)

print(f"The nth-order distance diff :{diff}")