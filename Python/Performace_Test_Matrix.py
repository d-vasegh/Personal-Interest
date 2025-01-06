import numpy as np
import cupy as cp
import time

# Create two random matrices of size 20,000 by 20,000 in NumPy
start_time = time.time()
matrix1 = np.random.rand(20000, 20000)
matrix2 = np.random.rand(20000, 20000)
end_time = time.time()
print(f"Creating 2 matrix in NumPy took {str(end_time-start_time)} seconds.")

# Multiply the two matrices to create a new matrix in NumPy
start_time = time.time()
result_matrix = np.dot(matrix1, matrix2)
end_time = time.time()
print(f"Matrix multiplication in NumPy took {str(end_time-start_time)} seconds.")

# Create two random matrices of size 20,000 by 20,000 in CuPy
start_time = time.time()
matrix1 = cp.random.rand(20000, 20000)
matrix2 = cp.random.rand(20000, 20000)
end_time = time.time()
print(f"Creating 2 matrix in CuPy took {str(end_time-start_time)} seconds.")

# Multiply the two matrices to create a new matrix in CuPy
start_time = time.time()
result_matrix = cp.dot(matrix1, matrix2)
end_time = time.time()
print(f"Matrix multiplication in CuPy took {str(end_time-start_time)} seconds.")
