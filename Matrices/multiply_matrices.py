   
#Given two square Matrices A[][] and B[][], stores the multiplied matrices in a new matrix C[][].
   
# Input: 
# N = 2
# A[][] = {{1, 2}, 
#         {3 , 4}}

# B[][] = {{-1, 3}, 
#          {4, 2}}

# Output: 
# C[][] = {{7, 7}, 
#          {13, 17}} 
   
import numpy as np

matrix_a = np.array([[1, 2], 
                     [3 , 4]], dtype=np.int64)

matrix_b = np.array([[-1, 3], 
                     [4, 2]], dtype=np.int64)

   
matrix_c = np.array([[0,0],[0,0]])

n=2
for i in range(n):
    for j in range(n):
        for k in range(n): #calcula prod. interno da linha i por coluna j
            matrix_c[i][j] = matrix_c[i][j] + (matrix_a[i][k] * matrix_b[k][j])

print(matrix_c)