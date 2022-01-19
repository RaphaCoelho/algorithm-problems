import numpy as np

matrix = np.array([[3,30,38], [44,52,54], [57,60,69]], dtype=np.int64)

X = 63
aux = 0
for row in matrix:
    for element in row:
        if X == element:
            #print('achou')
            aux = element
        #else:
            #print('não achou')
if aux != 0:
    print("Achou",aux)
else:
    print('Não achou')