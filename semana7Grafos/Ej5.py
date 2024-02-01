"""Implementar un algoritmo que convierta un grafo representado con matriz de adyacencia a un grafo
representado con listas de adyacencia"""

from GrafosLM import *
import numpy as np


def auto():
    lista = ['1,2', '1,3', '1,4', '2,1', '2,3', '2,5', '3,1', '3,4', '4,1', '4,3', '5,2', '5,4','6,1','6,2','6,4','1,6','2,6','4,6']
    matriz = np.zeros((6,6))
    for i in lista:
        pos = i.split(',')
        pos = list(map(int, pos))
        matriz[pos[0] - 1][pos[1] - 1] = 1

    return matriz
def crear_matriz():
    terminar = False
    while not terminar:
        try:
            print('------------------------------------------------')
            tam = int(input("Cuantos vertices tendra su grafo?:"))

        except (TypeError,ValueError):
            print("ingrese un valor valido")

        else:
            if tam <= 0:
                print("Una matriz no puede ser negativa, intente nuevamente")
            else:
                terminar = True
    if tam == 1:
        matriz = auto()
        return matriz
    matriz = np.zeros((tam, tam))
    terminar = False
    print('--------------------------------------------------------------------------')
    print("ingrese las posiciones en las que hay 1 de su matriz, separadas por una coma ej:2,3")
    print("ingrese un * para finalizar la carga ")
    print("La primer posicion de la matriz en 1,1")
    while not terminar:
        pos = input("posicion:")
        if pos == '*':
            terminar = True
        else:
            pos = pos.split(',')
            try:
                pos = list(map(int, pos))

            except ValueError:
                print('Error: posiciones invalidas')
            else:
                if len(pos) != 2 or pos[0] <= 0 or pos[0] > tam or pos[1] <= 0 or pos[1] > tam:
                    print("ingrese una posicion valida")
                else:
                    try:
                        matriz[pos[0]-1][pos[1]-1] = 1
                    except IndexError:
                        print("posicion fuera del rango de la matriz")
    return matriz


graph = Grafo()
print('De grafo reprecentado como mantriz de adyacencia a grafo reprecentado con lista de adyacencia')
print('Crear Matriz de adyacencias')
matriz = crear_matriz()
print("----------------------------------------")
print("Su Matriz de adyacencia:")
print(matriz)
print("----------------------------------------")
op = input("quiere ponerle nombre a cada uno de los vertices?(s/n):")
if op.lower() == 's':
    nombre = []
    for i in range(1,len(matriz)+1):
        nom = input(f"Nombre del vertice N°{i}:")
        nombre.append(nom)
    graph.de_matriz_a_lista(matriz,nombre)
else:
    graph.de_matriz_a_lista(matriz)
print("De su matriz se llego a la sigiente lista:")
graph.imprimir()
