"""Ejercicio 3
Implementar un algoritmo que calcule el grado de entrada y el grado de salida de un vértice. Calcular el
orden de complejidad para cada uno de los programas en el TAD que utiliza listas adyacentes y para el TAD
que utiliza matrices de adyacencia.
Grado de salida de un vértice: es el número de aristas que empiezan en el vértice.
Grado de entrada de un vértice: es el número de aristas que terminan en el vértice."""

from GrafosLM import *


def auto():
    coordenadas = ['1,2', '1,3', '1,4', '4,1', '4,2', '4,3', '5,1', '5,2', '5,3', '5,4']
    for i in coordenadas:
        pos = i.split(',')

        new_grafo.insertar(pos[0], pos[1], True)
    new_grafo.armar_matriz_desde_lista()
    return


def cargar_matriz():
    terminar = False
    while terminar is False:
        diri = False
        print('1)para autocargar')
        op = input("Es su grafo dirigido?(s/n):")
        if op.lower() == 's':
            diri = True
        if op == '1':
            auto()
            terminar = True
        print("ingrese las conexiones de su grafo separadas por una coma ej:2,3")
        print("ingrese un * para finalizar la carga ")

        while not terminar:
            pos = input("posicion:")
            if pos == '*':
                terminar = True
            else:
                pos = pos.split(',')

                if len(pos) != 2 :
                    print("ingrese una posicion valida")
                else:
                    new_grafo.insertar(pos[0], pos[1], diri)
    new_grafo.armar_matriz_desde_lista()
    return 0

def mostrargrados_todos():   #despues me di cuenta de que es solo para uno pero dejo esto para todos igual
    new_grafo.ver_matriz()
    IO = new_grafo.gradoIOMatriz_todos()
    print("Los grados usando la matriz:")
    print("Verticie - (entrada, salida)")
    for key, ensal in IO.items():
        print(f"\t{key}    -    {ensal}")

    print("Los grados usando la lista (son los mismos xd):")
    IO = new_grafo.gradoIOLista_todos()
    for key, ensal in IO.items():
        print(f"\t{key}    -    {ensal}")

def mostrargrados():
    terminar = False
    print("Mostrar grado de entrada y salida para un vertice")
    while terminar is False:
        print("--------------------------------------------")
        vertice = input("para el vertice:")
        if vertice == '*':
            terminar = True
        else:
            glista = new_grafo.gradosIOmatriz(vertice)
            gmatriz = new_grafo.gradoIOLista(vertice)
            if glista != False:
                print(glista)
                print(gmatriz)
            else:
                print("el vertice no existe")
        print("--------------------------------------------")
    op = input('desea ver todos los grados de entrada y de salida de todos los vertices? (s/n)')
    if op.lower() == 's':
        mostrargrados_todos()
    return
new_grafo = Grafo()
print("-- Grado de entrada y de salida -- ")
cargar_matriz()
print(new_grafo.imprimir())
mostrargrados()

print("El orden de complejidad a la hora de ver los grados de entrada y la salida con una matriz de adyacencia sera de")
print("O(n^2) ya que se tendra que recorrer toda la matriz para obtener los grados")
print("---")
print("Y el orden de complejidad para los grados en una lista de adyacencia sera de O(n+m)")
print("y por cada vertice para la salida se debera contar cuantos elementos tiene")
print("y para la entrada se debera ver en las demas listas de los otros vertices para ver en cuales aparece")
print("el vertice actual")
print("\n")
print("!!!!!!!!!!!!!!!!!")
print("Para la busqueda de solo un vertice a la vez matriz el grado de complejidad es lineal")