"""Ejercicio 6
Escribí una función para mezclar dos listas enlazadas. Las listas de entrada tienen sus elementos en orden
creciente, de menor a mayor. La lista de salida también debe quedar ordenada, pero de mayor a menor (orden
decreciente).
El algoritmo debería tomar tiempo lineal, según la longitud de la lista de salida, que es la suma de la longitud de
las dos listas.
L1 = [1, 12, 45, 46]
                                L3 = [100, 80, 60, 46, 45, 40, 20, 12, 1, 0]
L2 = [0, 20, 40, 60, 80, 100]"""

from ListasEnlazadas import *
import random

def automatico():
    for i in range(0, random.randrange(5, 15)):
        L1.agregar_nodo(random.randrange(0, 70))

    for i in range(random.randrange(3, 15)):
        L2.agregar_nodo(random.randrange(0, 70))

    L3 = L1.mesclarlistas(L2, True)


    return L1, L2, L3

def amano():
    dato = 0
    print("ingrese un * para terminar de llenar")
    print("Llenar la primer lista\n")

    while dato != '*':
        dato = input("dato:")
        if dato != '*':
            L1.agregar_nodo(dato)
    print("\nLlenar segunda lista")
    dato = 0
    while dato != '*':
        dato = input("dato:")
        if dato != '*':
            L2.agregar_nodo(dato)

    L3 = L1.mesclarlistas(L2, True)  #True para decirle que sea de mayor a menor
    return L3

terminar = False
while terminar == False:
    L1 = ListaEnlazada()
    L2 = ListaEnlazada()
    print("-- llenar dos listas con enteros, mesclarlas y devolver una tercer listar ordenada de mayor a menor -- ")
    try:
        op = int(input("1)llenar automaticamente\n2)llenar a mano\n3)salir\nop:"))
    except ValueError:
        print("Error, opcion incorrecta")
    else:
        if op == 1:
            L1, L2, L3= automatico()
            print("------------------------------------------------")
            print("L1:")
            L1.imprimirLista()
            print("L2:")
            L2.imprimirLista()
            print("Lista mesclada:")
            L3.imprimirLista()
            print("------------------------------------------------")
        elif op == 2:
            L3 = amano()
            L3.imprimirLista()
        elif op == 3:
            terminar = True
        else:
            print("opcion incorrecta intente nuevamente")
print("Saliendo")
#dar vuelta l3







