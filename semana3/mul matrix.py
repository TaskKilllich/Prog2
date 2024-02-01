import random

def multi(matrizA,matrizB,filasA,columnasB):
    matrizC = [[0 for _ in range(columnasB)] for _ in range(filasA)]  # crea una matriz llena de 0 para luego poner los resultados donde van
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
        #orden O(n^3) causa de los 3 fors para recorrer ambas matrices
    return matrizC

def llenarmatrizes(filasA,columnasA,filasB,columnasB):
    matrizA=[]
    matrizB=[]
    for i in range(filasA):
        matrizA.append([])
        for j in range(columnasA):
            matrizA[i].append(random.randint(0, 10))
    # llena las matrices con numeros random dependiendo del tamaño
    #  O(n^2)
    for i in range(filasB):
        matrizB.append([])
        for j in range(columnasB):
            matrizB[i].append(random.randint(0, 10))
     # O(n^2)
    return matrizA,matrizB

print("Multiplicador de matrizes")
print("Matriz A")
filasA = int(input("ingrese la cantidad de filas:"))
columnasA = int(input("ingrese la cantidad de columnas:"))
print("Matriz B")
filasB = int(input("ingrese la cantidad de filas:"))
columnasB = int(input("ingrese la cantidad de columnas:"))
if columnasA!=filasB:
    print("el numero de columnas de la matriz A tiene que ser igual al numero de filas de la Matriz B")
else:
    matrizA,matrizB = llenarmatrizes(filasA,columnasA,filasB,columnasB)
    print(matrizA,"\n",matrizB)
    matrizC=str(multi(matrizA,matrizB,filasA,columnasB))
    print(matrizC)

