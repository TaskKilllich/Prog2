"""Ejercicio 4
Listar los vértices de un grafo que tienen grado de salida 0. Estos vértices se llaman sumideros.
Listar los vértices del grafo que tienen grado de entrada 0. ¿Puede hacer algún comentario respecto a
estos vértices?"""
from GrafosLM import *

def auto():
    coordenadas = ['1,2','1,3','1,4','4,1','4,2','4,3','5,1','5,2','5,3','5,4']
    for i in coordenadas:
        pos = i.split(',')
        pos = list(map(int, pos))
        new_grafo.insertar(pos[0], pos[1], True)
    return


def armar_grafo():
    terminar = False
    while terminar is False:
        diri = False
        print("si no es dirigido no habra sumideros")
        print("  1)para autocargar")
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

                if len(pos) != 2:
                    print("ingrese una posicion valida")
                else:
                    new_grafo.insertar(pos[0], pos[1], diri)

new_grafo = Grafo()
armar_grafo()
print("-- Grado de entrada y de salida -- ")
print("A un vertice con grado de entrada 0 pero grado de salida != 0 se lo llamara vertice de salida o fuente exterior")
print(new_grafo.sumideros())
new_grafo.imprimir()
print("#para que un sumidero o una fuente exista el grafo debe ser dirigido")