"""Ejercicio 2
Se puede formular recursivamente la suma de los n primeros números naturales. Diseñar una función recursiva en
Python que calcule la sumatoria de los n primeros números naturales, según la fórmula:"""


def sumatoria(num):
    if num== 1:
        return 1
    else:
        return num + sumatoria(num-1)

num = 1
while num != 0:
    print("**Ingrese un 0 para terminar")
    print("suma de los n primeros numeros naturales")
    num = int(input("hasta que n quiere sumar?:"))
    if num != 0:
        print('La sumatoria de 1 a {} es = {}'.format(num,sumatoria(num)))
    else:
        print("Saliendo...")





