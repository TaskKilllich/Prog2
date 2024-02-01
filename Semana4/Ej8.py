"""Ejercicio 8
Escribir una función espejo(q) que acepte una cola de letras como parámetro y que agregue los elementos al final
de la cola en orden inverso, formando un string “capicúa”:
Ejemplo: a b c d → a b c dd c b a
Considere usar una pila como estructura auxiliar."""

from Cola import *

def espejo(cadena):
    for i in cadena[::-1]:
        new_pila.encolar(i)

    print(cadena, end='')

    while not new_pila.empty():
        print(new_pila.desencolar(), end='')

    return 0


new_pila = Cola()

print("Capicúa    ej: a b c d -> a b c d d c b a")
cadena = input("Ingrese su cadena:")
espejo(cadena)
