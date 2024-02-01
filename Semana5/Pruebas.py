from ListasEnlazadas import *
from random import *

palabras = {'Elefante','Perplejidad','Melodía','Esmeralda','Plenitud','Quimera',1888,1997}
nodo = ListaEnlazada()
for i in palabras:
    nodo.agregar_nodo(i)

op = 1
nodo.imprimirlistanumerada()
op = input("intercambiar por pos:")
nodo.intercabiar(None,True,int(op))
nodo.imprimirlistanumerada()
"""while op != 0:
    nodo.imprimirlistatareas()
    op = int(input("borrar:"))
    nodo.borrar_por_posicion(op-1)
    nodo.imprimirlistatareas()
"""
"""Nodo1 = Nodo("tomate",1)

Nodo2 = Nodo("pera")

Nodo3 = Nodo("lechuga")

Nodo1.prox = Nodo2
Nodo2.prox = Nodo3


print(Nodo1.dato)
print(Nodo1.prox)
print(Nodo1.prox.prox)"""
