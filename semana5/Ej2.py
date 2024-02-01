"""Ejercicio 2
Creá un método imprimir() que extienda la clase ListaEnlazada y que imprima la lista siguiendo el mismo formato
de las listas de Python. Utilizá para ello el método imprimeLista(nodo) definido en la teoría.
#>>> print(L1)
[] # Si L1 está vacía
#>>> print(L1)
[0, 2, 123] # Imprimir los valores entre corchetes, separados con comas."""


from ListasEnlazadas import *

def agregaralista():
    terminar = False
    print("Ingrese un * para terminar la carga")
    while terminar == False:
        elemento = input("su elemento:")
        if elemento != '*':
            nodo.agregar_nodo(elemento)
        else:
            print('terminando carga...')
            terminar = True
    return

nodo = ListaEnlazada()
print("Implementacion del imprimir() -> [su,elementos,aca]")
agregaralista()
print("su lista enlazada")
nodo.imprimirLista()
