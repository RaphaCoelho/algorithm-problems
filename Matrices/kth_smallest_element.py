#Given a N x N matrix, find the kth smallest element in the matrix.

# Input:
# N = 4
# mat[][] =          {{16, 28, 60, 64},
#                    {22, 41, 63, 91},
#                    {27, 50, 87, 93},
#                    {36, 78, 87, 94 }}
# K = 3
# Output: 27
# Explanation: 27 is the 3rd smallest element.

import numpy as np
n = 4
matrix = np.array([[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93],[36, 78, 87, 94]], dtype=np.int64)
k = 3
aux = 0
array = []

for i in range(0,n,1):
    for j in range(0,n,1):
        if len(array) < k:
            array.append(matrix[i][j])
        else:
            for element in range(n):
                for element in range(0,k-1,1):
                    next_element=element+1
                    if array[next_element] < array[element]:
                        array[element],array[next_element] = array[next_element],array[element]
            if matrix[i][j] < array[k-1]:
                array[k-1] = matrix[i][j]   

print(k,'º menor elemento: ', array[k-1])
print(array)
