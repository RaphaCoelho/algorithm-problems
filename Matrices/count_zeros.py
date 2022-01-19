# Given a N X N binary Square Matrix where each row and column of the matrix. 
# Find the total number of zeros present in the matrix.

# Input:
# N = 3
# A = {{0, 0, 0},
#      {0, 0, 1},
#      {0, 1, 0}}
# Output: 6
# Explanation: 
# The first, second and third row contains 3, 2 and 1
# zeroes respectively.

import numpy as np
n=3
matrix = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=np.int64)
count_zeros = 0

for row in matrix:
    for element in row:
        if element == 0:
            count_zeros =+ count_zeros+1
print(count_zeros)