# Question 6
import numpy as np

# create the two arrays
arr1 = np.array([0, 1, 2])
arr2 = np.array([2, 1, 0])

# compute the covariance matrix
cov_matrix = np.cov(arr1, arr2)

print("Array1:", arr1)
print("Array2:", arr2)
print("Covariance des 2 arrays:", cov_matrix)
