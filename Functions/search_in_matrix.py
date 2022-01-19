import numpy as np

matrix = np.array([[3,30,38], [44,52,54], [57,60,69]], dtype=np.int)

X = 62
def search_matrix(X, matrix):
    for row in matrix:
        for element in row:
            if X == element:
                return print("Achou!")
        
    print("Não achou!")

search_matrix(X,matrix)