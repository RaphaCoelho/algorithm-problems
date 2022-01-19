# Given a square matrix of size N*N, print the sum of upper and lower triangular elements. 
# Upper Triangle consists of elements on the diagonal and above it. 
# The lower triangle consists of elements on the diagonal and below it. 

# Input:
# N = 3 
# mat[][] = {{6, 5, 4},
#            {1, 2, 5}
#            {7, 9, 7}}
# Output: 29 32
# Explanation:
# The given matrix is
# 6 5 4
# 1 2 5
# 7 9 7
# The elements of upper triangle are
# 6 5 4
#   2 5
#     7
# Sum of these elements is 6+5+4+2+5+7=29
# The elements of lower triangle are
# 6
# 1 2
# 7 9 7
# Sum of these elements is 6+1+2+7+9+7= 32.

import numpy as np
n = 3
matrix = np.array([[6, 5, 4], [1, 2, 5], [7, 9, 7]], dtype=np.int64)

upper_triangle = 0
lower_triangle = 0

for i in range(0,n,1):
    for j in range(n-1,-1,-1):
        if i == j:
            upper_triangle =+ upper_triangle + matrix[i][j]
            lower_triangle =+ lower_triangle + matrix[i][j]
        elif j > i:
            upper_triangle =+ upper_triangle + matrix[i][j]
        elif j < i:
            lower_triangle =+ lower_triangle + matrix[i][j]

print('triangulo superior', upper_triangle)
print('triangulo inferior', lower_triangle)