"""Ejercicio 3
Escribir un programa que lea una secuencia de caracteres y los imprima en orden inverso, usando el TAD Pila. La
secuencia termina al ingresar un * (asterisco).
Analizar la eficiencia del algoritmo resultante, buscando la función que representa el código y la cota superior (peor
caso)."""

from Pila import *

def inverso():
    print("\nsecuencia ingresada: {}".format(' '.join(new_pila.elementos)))
    print("secuencia inversa: ",end='')
    while not new_pila.empty():
        print(new_pila.elementos.pop(),end=' ')
    return 0


new_pila = Pila()
print("programa que imprime la secuencia de caracteres usted le da, al revez")
print("Termina la carga de caracteres con un *")
caracter = 1
while caracter != '*':
    caracter = input("Ingrese su caracter:")
    if caracter != '*':
        new_pila.push(caracter)

inverso()
