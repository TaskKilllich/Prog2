"""Ejercicio 6
Implementar un algoritmo que convierta un grafo representado con listas de adyacencia a un grafo
representado con matriz de adyacencia."""

from GrafosLM import *


def armar():
    terminar = False
    isdiri = False
    print("arme el grafo se deberia llenarse como 'origen,destino' separado por coma")
    print("- Ingerse un * para terminar")
    diri = input("esta por armar un grafo dirigido?(s/n):")
    if diri.lower() == 's':
        print('ss')
        isdiri = True

    while not terminar:
        origendestino = input("origen,destino:")
        if origendestino == '*':
            terminar = True
        else:
            origendestino = origendestino.split(',')

            if len(origendestino) != 2:
                print("Error: origen o destino mal cargado")
            else:
                graph.insertar(origendestino[0],origendestino[1],isdiri)
    return


graph = Grafo()
print("-- De Lista a matriz -- ")
armar()
print("Su lista de adyacencias:")
graph.imprimir()
print('---------------------------')
print("La matriz resultante")
graph.armar_matriz_desde_lista()
print(graph.ver_matriz())








