"""Ejercicio 5
Escribir un programa que valide los paréntesis de una expresión usando una pila, y devuelva “correcta” en caso de
que los paréntesis estén correctamente utilizados, e “incorrecta” para aquellos casos en que haya un error.
Ejemplo Resultado
- Correcta (la expresión vacía está bien formada)
- () Correcta
- (()(())) Correcta
- )( Incorrecta
- (() Incorrecta
- ()) Incorrecta
- ((2+x)*23)/(6+x) Correcta
- 2x+101)/12 Incorrecta
    if not new_pila.empty():
        equilibrio = False"""

from Pila import *


def evaluar():
    equilibrio = True
    for i in cadena:
        if i == '(':
            new_pila.push(i)
        elif i == ")":
            if not new_pila.empty():
                new_pila.pop()
            else:
                equilibrio = False
    if not new_pila.empty():
        equilibrio = False

    return equilibrio

print("Programa que evalua los parentecis (()))")

cadena = 1
while cadena != '*':
    print("--ingrese un * para terminar")
    new_pila = Pila()
    cadena = input("ingrese su cadena para evaluar sus parentecis:")
    if cadena != '*':
        res = evaluar()
        print("---------------------------------------------------")
        if res == True:
            print("la expresion {} es correcta, esta equilibrada con respecto a los parentecis".format(cadena))
        else:
            print("la expresion {} es incorrecta, no equilibrada con respecto a los parentecis".format(cadena))
        print("---------------------------------------------------")
    else:
        print("saliendo...")