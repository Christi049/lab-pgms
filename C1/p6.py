"""Read and display a sparse matrix using dictionary
"""
rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

sparse_matrix = {}

for i in range(rows):
  for j in range(cols):
    val = int(input(f"Enter element at {i},{j} :"))
    if val!= 0:
      sparse_matrix[(i,j)] = val

print("the sparse matrix dictionary :")
print(sparse_matrix)

for i in range(rows):
  for j in range(cols):
    print(sparse_matrix.get((i,j),0), end=' ')
  print()