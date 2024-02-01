"""Ejercicio 3
Escriba dos métodos NO recursivos que encuentren:
(a) El mínimo de un ABB
(b) El máximo de un ABB"""

from ArbolBB import *
from random import randrange
from ImprimirABBtortuga import *

def cargararbol():
    terminar = False
    while terminar == False:
        try:
            valor = int(input("valor:"))
        except ValueError:
            terminar = True
        else:
            new_arbol.insertar(valor)
    return

def autocarga():
    new_arbol.insertar(randrange(15, 27))
    for i in range(randrange(4, 10)):
        new_arbol.insertar(randrange(0, 40))
    return

def mostrar():
    print("valor maximo:", new_arbol.maximo())
    print("valor minimo:", new_arbol.minimo())
    canvas = Screen()
    turtle.TurtleScreen._RUNNING = True  # sin esto al momento de hacer un nuevo arbol en la misma ejecucion la tortuga da error
    ImprimirABT(new_arbol)
    canvas.exitonclick()

op = 0
while op != 3:
    new_arbol = ArbolBB()
    print("-- Valor Maximo y Minimo de un arbol --")
    print("1) llenar arbol automaticamente")
    print("2) llenar arbol a mano")
    print("3) Salir")
    op = int(input("op:"))
    if op == 1:
        autocarga()
        mostrar()
    elif op == 2:
        new_arbol = cargararbol()
        mostrar()
    elif op == 3:
        print("Saliendo")
    else:
        print("Opcion incorrecta intente nuevamente")





















