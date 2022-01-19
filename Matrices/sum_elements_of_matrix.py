# Given a non null integer matrix Grid of dimensions NxM.Calculate the sum of its elements.
# Input:
# N=2,M=3
# Grid=
# [[1,0,1],
# [-8,9,-2]]
# Output:
# 1
# Explanation:
# The sum of all elements of the matrix is 
# (1+0+1-8+9-2)=1.


import numpy as np

matrix = np.array([[3,30,38], 
                   [44,52,54], 
                   [57,60,69]], dtype=np.int64)

soma = 0
for row in matrix:
    for element in row:
        soma =+ soma+element

print('Total',soma)