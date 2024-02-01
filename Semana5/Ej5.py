"""Ejercicio 5
Usando el TAD ListaEnlazada, escribí una función para intercambiar el elemento x con el elemento siguiente en la
lista. Si x es el último elemento, la lista debe permanecer sin modificaciones"""

from ListasEnlazadas import *

def cargarlista():

    palabras = {'Elefante', 'Perplejidad', 'Melodía', 'Esmeralda', 'Plenitud', 'Quimera', 1888, 1997}
    print("Agregar elementos a la lista")
    elemento = input("apriete 1 para cargar elementos al azar\n-- use un * paraterminar\nelemento:")

    if elemento == "1":
        for i in palabras:
            lista.agregar_nodo(i)
        return
    while elemento != '*':
        if elemento != '*':
            lista.agregar_nodo(elemento)
            elemento = input("elemento:")
    return

def intercambiar():
    print("___ Intercambiar los elementos ___")
    lista.imprimirlistanumerada()
    op = int(input("1) Intercambiar por nombre\n2) Intercambiar por posicion\nop:"))
    if op == 1:
        print("asegurese de escribirlo igual")
        eleainter = input("elemento:")
        lista.intercabiar(eleainter)
    elif op == 2:
        posicion = int(input("posicion:"))
        lista.intercabiar(None, True, posicion)
    lista.imprimirlistanumerada()
    return


lista = ListaEnlazada()
print("--- Intercambiar un elemento de una lista por el siguiente ---\n")

cargarlista()
op = 0
while op != 'n':
    intercambiar()
    op = input("Seguir intercambiando?[y/n]")
    op = op.lower()

print("Saliendo...")


