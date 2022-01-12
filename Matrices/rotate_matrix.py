import numpy as np

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype=np.int)

matrix_result = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype=np.int)

N = 3
k = 0
i = 0 
aux=[]
for row in matrix:
    for r in row:
        aux.append(r)
        print('aux:',aux)
    for j in range(N-1,-1,-1):
        matrix_result[j][i] = aux[0]
        aux.pop(0)

    i+=1


print('matrix inicial:\n',matrix)
print('matrix final:\n',matrix_result)