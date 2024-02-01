"""Ejercicio 6
Escriba una función recursiva llamada imprimirRango que, dado un ABB, un valor_bajo y un valor_ alto, imprima
en forma ordenada todos los nodos cuyos valores estén entre valor_bajo y valor_alto. La función debería visitar la
menor cantidad de nodos posibles en el ABB."""
import turtle

from ArbolBB import *
from random import randrange
from ImprimirABBtortuga import *


def autocarga():
    new_arbol.insertar(randrange(15, 27))
    for i in range(randrange(4, 10)):
        new_arbol.insertar(randrange(0, 40))


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


def rango():
    op = input("imprimir arbol?(s/n)")
    if op.lower() == 's':
        print("Porfavor espere mientras se dibuja el arbol cuando se termine de dibujar cierre haciendo click")
        ImprimirABT(new_arbol)
    canvas = Screen()
    turtle.TurtleScreen._RUNNING = True  # sin esto al momento de hacer un nuevo arbol en la misma ejecucion la tortuga da error
    min = int(input("min:"))
    max = int(input("max:"))
    recorrido = imprimirRango(new_arbol, min, max)
    if recorrido is False:
        print("El arbol esta vacio")
    else:
        print("el recorrido fue:")
        print(recorrido)

    canvas.exitonclick()
    return


op = None
while op != 3:
    new_arbol = ArbolBB()
    print("-- Rango --")
    print("1) llenar arbol automaticamente")
    print("2) llenar arbol a mano")
    print("3) Salir")
    op = int(input("op:"))
    if op == 1:
        autocarga()
        rango()
    elif op == 2:
        cargararbol()
        rango()
    elif op == 3:
        print("Saliendo")
    else:
        print("Opcion incorrecta intente nuevamente")
