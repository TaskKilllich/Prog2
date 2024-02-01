import numpy as np

lista = {'b': ['a', 'c', 'd'],
         'a': ['b', 'c', 'd'],
         'c': ['e', 'd'],
         'e': ['a','d'],
         'z':['a','j','z']}

# Obtener la lista de letras únicas en el diccionario
letras_unicas = sorted(list(set(lista.keys()) | set(sum(lista.values(), []))))


# Crear la matriz de adyacencia
matriz = np.zeros((len(letras_unicas), len(letras_unicas)))

# Llenar la matriz de adyacencia
for origen, destinos in lista.items():
    print('des',destinos)
    for destino in destinos:
        fila = letras_unicas.index(origen)
        columna = letras_unicas.index(destino)

        matriz[fila, columna] = 1

print(matriz)