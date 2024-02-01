"""Ejercicio 1
Implementar la clase grafo, utilizando matrices de adyacencia, con los mismos métodos que se incluyeron
para la implementación con listas de adyacencia."""

from GrafosMatrices import *


def auto():
    coordenadas = ['1,2', '1,4', '1,5', '2,3', '2,4', '3,4', '4,5', '5,2']
    for i in coordenadas:
        pos = i.split(',')
        pos = list(map(int, pos))
        new_grafo.insertar_en_matriz(pos[0]-1, pos[1]-1)
    return


def cargar_matriz():
    terminar = False
    while terminar is False:
        diri = False
        op = input("Es su grafo dirigido?(s/n)")
        if op.lower() == 's':
            diri = True

        print("ingrese las conexiones de su grafo para armar la matriz separadas por una coma ej:2,3")
        print("ingrese un * para finalizar la carga ")

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
                    if len(pos) != 2 and tam < pos[0] < 0 > pos[1] > tam:
                        print("ingrese una posicion valida")
                    else:
                        new_grafo.insertar_en_matriz(pos[0]-1, pos[1]-1, diri)


print("-- Matrices de adyacencia -- ")
print(" -- Arme su grafo utilizando matriz de adyacencia -- ")
print("La primer posicion de la matriz es la 1,1")
terminar = False
while terminar is False:
    print("--------------------------------------------------------------")
    try:
        tam = int(input("(1 para autollenar)\nTamaño de su matriz:"))
    except ValueError:
        print("Valor invalido intente nuevamente")
    else:
        if tam == 1:
            new_grafo = Grafo(5)
            auto()
            terminar = True
        elif tam > 1:
            new_grafo = Grafo(tam)
            cargar_matriz()
            terminar = True
        else:
            print("El tamanio debe ser un entero positivo")

new_grafo.ver_matriz()
terminar = False
while terminar is False:
    print("--------------------------------------------------------------")
    print("Probar BFS para que numero? \n- Ingrese un * para salir")
    num = input("Numero:")
    if num == '*':
        terminar = True
    else:
        try:
            num = int(num) - 1  #porque en realidad la matriz es de 0 hasta n
        except TypeError:
            print("Error. Ingrese un entero")
        else:
            new_grafo.bfs(num)
            print('')
print("Para obtener los adyacentes se debe recorrer la matriz, segun el vertice elegido")
print("Los cambios que se hicieron fueron para obtener el adyacente ya que este se encuentra en la matriz")