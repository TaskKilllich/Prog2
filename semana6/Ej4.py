"""Ejercicio 4
Dado un árbol binario, se desea determinar si es de búsqueda o no. Implemente una función que lo recorra y
devuelva False si no es un ABB, y True si realmente lo es."""

from ArbolBB import *
from random import randrange
from ImprimirABBtortuga import *

def cargararbolbusqueda():
    terminar = False
    while terminar == False:
        try:
            valor = int(input("valor:"))
        except ValueError:
            terminar = True
        else:
            new_arbol.insertar(valor)

    print("Carga completa...\n")
    return

def cargararbolNObusqueda():
    terminar = False
    while terminar == False:
        try:
            valor = int(input("valor:"))
        except ValueError:
            terminar = True
        else:
            new_arbol.insertar_no_bus(valor)

    print("Carga completa...\n")
    return

def autocarga():
    new_arbol.insertar(randrange(15, 27))
    sera_busqueda = randrange(0,2)
    if sera_busqueda == 1:
        for i in range(randrange(4, 10)):
            new_arbol.insertar(randrange(0, 40))
    else:
        for i in range(randrange(4, 10)):
            new_arbol.insertar_no_bus(randrange(0, 40))
    print("Carga completa...\n")

    return

def esbusqueda():

    respuesta = es_busqueda_recursivo(new_arbol)
    print("------------------------------------")
    if respuesta is False:
        print("El arbol no es de busqueda")
    else:
        print("El arbol es de busqueda")
    print("------------------------------------")
    canvas = Screen()
    turtle.TurtleScreen._RUNNING = True  # sin esto al momento de hacer un nuevo arbol en la misma ejecucion la tortuga da error
    ImprimirABT(new_arbol)
    canvas.exitonclick()
    return

def imprimir():
    esbusqueda()
    new_arbol = ArbolBB()
    return

op = 0
new_arbol = ArbolBB()
while op != 3:
    print("--- Determinar si un arbol binario es de busqueda o no ---")
    print("-Por la naturaleza de como se cargan los datos de forma ordenada simpre sera de busqueda por lo cual se implementa un random al momento de cargar los datos para que el Arbol sea ABB o no")
    print("1) llenar arbol automaticamente")
    print("2) llenar arbol a mano")
    print("3) Salir")
    op = int(input("op:"))
    if op == 1:
        autocarga()
        imprimir()
    elif op == 2:
        sera_busqueda = randrange(0, 2)
        if sera_busqueda == 1:
            cargararbolbusqueda()
        else:                       #por como el insert carga los datos siempre iba a ser de busqueda
            cargararbolNObusqueda()
        imprimir()
    elif op == 3:
        print("Saliendo")
    else:
        print("Opcion incorrecta intente nuevamente")









