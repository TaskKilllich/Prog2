"""Ejercicio 6
Se les solicita escribir una función max(s) que acepta una pila de enteros s y devuelve su mayor elemento, es decir
el entero mayor en la pila. ¿Qué hay que tener en cuenta para resolver este ejercicio?
Resolver y calcular el orden de complejidad de la función max(s) resultante."""

from Pila import *


def max():
    if new_pila.empty():
        new_pila.push(None)       #agrego un None si al momento de cargar los datos se no se ingreso ninguno
    while not new_pila.empty():
        num1 = new_pila.pop()
        if not new_pila.empty():
            num2 = new_pila.pop()
            if num1 > num2:
                new_pila.push(num1)
            else:
                new_pila.push(num2)
    new_pila.push(num1)
    return 0


def llenarpila():
    num = 1
    print("ingrese un * para terminar")
    while num != "*":
        num = input("num:")
        if num != "*":
            try:
                num = int(num)
            except ValueError:
                print("--'Error ingrese un numero entero")
            else:
                new_pila.push(num)
        else:
            print("llenado terminado")
    return 0

new_pila = Pila()

print("Programa que devuelve el mayor de los numeros ingresados, mediante el uso de una pila")
llenarpila()
print(new_pila.elementos)
max()

print("el elemento mas grande que habia en la pila era un:",new_pila.pop())
print("El orden de complejidad del ejercicio es O(n), dependera del tamano de la pila")


