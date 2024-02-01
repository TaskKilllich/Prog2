"""Ejercicio 8
Definir una función recursiva, cuenta_atras(n), que recibe un número natural y cuenta hacia atrás desde ese
número hasta cero. Cuando llega al final de la cuenta, en vez de imprimir el 0, muestra la palabra “Despegando!”."""


def cuenta_atras(n):
    if n == 0:
        print("despegando...")
    else:
        print(n)
        return cuenta_atras(n-1)
try:
    n = int(input("ingrese un numero natural:"))
    if n<0:
        cuenta_atras(n)
    else:
        print("Los Naturales son positivos")
except ValueError:
    print("Usted no ingreso un numero natural")



