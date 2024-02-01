"""Ejercicio 3
Escribí un método iguales(). Dos listas enlazadas se consideran iguales si contienen los mismos nodos (no el
mismo objeto nodo, sino nodos con los mismos datos), en el mismo orden. Utilizá el siguiente algoritmo:
1. Comparar el tamaño de las dos listas, si no tienen la misma longitud, es imposible que sean iguales.
2. Si las listas son de la misma longitud, comparar cada nodo de una lista con el de la misma posición
relativa de la otra lista.
3. Si cualquiera de los nodos es diferente, este método debe devolver “False”.
4. Si se terminó de chequear todos los nodos y todos son iguales, el método debe devolver “True”."""

from ListasEnlazadas import *

def llenarlistas():
    terminar = False
    print("---- Llenado de las listas ----")
    print("Llenar la primer listas")
    print("--ingrese un * para terminar la carga")
    while terminar == False:
        elemento = input("elemento:")
        if elemento != '*':
            nodo1.agregar_nodo(elemento)
        else:
            print('terminada la carga de la primer lista')
            terminar = True

    terminar = False

    print("Llenar la segunda listas")
    print("--ingrese un * para terminar la carga")
    while terminar == False:
        elemento = input("elemento:")
        if elemento != '*':
            nodo2.agregar_nodo(elemento)
        else:
            print('terminada la carga de la segunda lista')
            terminar = True

op = '1'
while op != 'N':
    nodo1 = ListaEnlazada()
    nodo2 = ListaEnlazada()

    print("--- Comparar 2 Listas ---")
    llenarlistas()
    retorno = nodo1.iguales(nodo2)
    print("---------------------------------")
    if retorno == False:

        print("Las listas no son iguales")
    else:
        print("Ambas listas son iguales")
    print("_________________________________")
    op = input("Comparar otro par de listas?[S/N]")
    op = op.upper()

print("Saliendo")
