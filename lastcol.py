import numpy as np

# Example 2-dimensional Numpy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract the last column of the matrix
last_column = matrix[:, -1]

print("Original matrix:")
print(matrix)
print("\nLast column of the matrix:")
print(last_column)
