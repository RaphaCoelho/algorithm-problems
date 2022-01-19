#Given a matrix of size N x N. Print the elements of the matrix in the snake pattern.

# Input:
# N = 3 
# matrix[][] = {{45, 48, 54},
#              {21, 89, 87}
#              {70, 78, 15}}
# Output: 45 48 54 87 89 21 70 78 15 
# Explanation:
# Matrix is as below:
# 45 48 54
# 21 89 87
# 70 78 15
# Printing it in snake pattern will lead to 
# the output as 45 48 54 87 89 21 70 78 15.

import numpy as np

#matrix = np.array([[45, 48, 54], [21, 89, 87], [70, 78, 15]], dtype=np.int64)
matrix = np.array([[45, 48, 54, 15], [21, 89, 87,16], [70, 78, 15,17],[14,23,37,80]], dtype=np.int64)
n = 4
result_set = []
for i in range(0,n,1):
    if i%2 == 0:
        for j in range(0,n,1):
            result_set.append(matrix[i][j])
    else:
        for j in range(n-1,-1,-1):
            result_set.append(matrix[i][j])
            
print(result_set)
# for i in range(n-1,-1,-1):
#     print(i)