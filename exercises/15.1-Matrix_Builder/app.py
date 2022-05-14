#Import random
import random
#Create the function below:
def matrixBuilder(num):
    matrix = []
    for i in range(0,num):
        matAux = []
        for j in range(0,num):
            matAux.append(1)
        matrix.append(matAux)
    return matrix


print(matrixBuilder(3))

