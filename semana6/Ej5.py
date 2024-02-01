"""Ejercicio 5
Implemente un método para borrar un nodo de un ABB. Puede seguir los pasos de la Teoría. Cargue el árbol del
ejemplo y verifique que el algoritmo funciona correctamente para cada uno de los tres casos."""

from ArbolBB import *
from random import randrange
from ImprimirABBtortuga import *
def autocarga():
    nodos = [2,1,7,8,4,6,3,5]
    for i in nodos:
        new_arbol.insertar(i)
    return

def cargararbol():
    terminar = False
    while terminar is False:
        try:
            valor = int(input("valor:"))
        except ValueError:
            terminar = True
        else:
            new_arbol.insertar(valor)
    return

def borrar_valor():
    valor = int(input("valor a borrar:"))
    res = new_arbol.borrar_nodo(valor)
    if res is False:
        print("El nodo no existe o esta queriendo borrar la raiz")
    else:
        print(f"el valor:{valor} a sido borrado")

def imprimir():
    op = int(input("1)Imprimir solo los elementos\n2)Imprimir de forma grafica\nop:"))
    if op == 1:
        print("Elementos:")
        new_arbol.imprimir()
        print('\n')
    elif op == 2:
        print("Espere a que el arbol se termine de dibujar y luego cierre para continuar")
        canvas = Screen()
        turtle.TurtleScreen._RUNNING = True  # sin esto al momento de hacer un nuevo arbol en la misma ejecucion la tortuga da error
        ImprimirABT(new_arbol)
        canvas.exitonclick()
    else:
        print("Opcion no valida")
    return

op = 0

new_arbol = ArbolBB()
while op != 5:
    print("-- Borrar elementos del ArbolBB --")
    print("1) llenar arbol del ejemplo de la teoria")
    print("2) cargar un arbol distinto")
    print("3) borrar un nodo del arbol")
    print("4) Imprimir arbol")
    print("5) Salir")
    op = int(input("op:"))
    if op == 1:
        autocarga()
    elif op == 2:
        cargararbol()
    elif op == 3:
        borrar_valor()
    elif op == 4:
        imprimir()
    elif op == 5:
        print("Saliendo...")
    else:
        print("Opcion incorrecta intente nuevamente")






