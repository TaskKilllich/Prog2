"""Ejercicio 2
Escriba una función recursiva que devuelva la cantidad de hojas de un árbol binario."""

from ArbolBB import *
from random import randrange
from ImprimirABBtortuga import *

def cargararbol():
    terminar = False
    print('-terminar llenado con un *')
    print('-Lenar solo con valores enteros')
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
    for i in range(randrange(5, 13)):
        new_arbol.insertar(randrange(0, 40))
    return

def imprimir():
    print(f'La cantidad de hijos es de: {contarhojas(new_arbol)}')
    canvas = Screen()
    turtle.TurtleScreen._RUNNING = True         #sin esto al momento de hacer un nuevo arbol en la misma ejecucion la tortuga da error
    ImprimirABT(new_arbol)
    canvas.exitonclick()
    return

op = 0
while op != 3:
    new_arbol = ArbolBB()
    print("-- contar cuantas hojas tiene el arbol --")
    print("1) llenar arbol automaticamente")
    print("2) llenar arbol a mano")
    op = int(input("op:"))
    if op == 1:
        autocarga()
        imprimir()
    elif op == 2:
        cargararbol()
        imprimir()
    else:
        print("Opcion incorrecta intente nuevamente")


"""      1
    0           7
            5       9   
                        10
      
      """


