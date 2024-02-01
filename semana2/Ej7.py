"""Ejercicio 7
Implementar las tres variantes del algoritmo para calcular la sucesión de Fibonacci vistas en clase (recursiva,
iterativa, por fórmula).
Luego escribir una función que pida un número, ejecute las tres versiones del cálculo, y para cada una de ellas
mida cuánto tarda la ejecución. Se recomienda calcular valores grandes de números de Fibonacci, n>30
Para medir tiempo de ejecución, Python cuenta con varias funciones. Investigue time(), perf_counter() y
process_time(), funciones del módulo time que permiten este tipo de cálculos. Elija una, y justifique por qué la
eligió."""


from decimal import *
from math import sqrt
from math import pow
from time import perf_counter

def fibo_recu(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibo_recu(num-1) + fibo_recu(num-2)


def fibo_iter(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        f1 = f2 =1
        for i in range(3, num+1):
            f=f1+f2
            f1,f2 = f2,f
    return f


def fibo_formula(num):

    #f = ((1/(sqrt(5)))*((((1+sqrt(5))/2)**num)-(((1-sqrt(5)))/2)**num))
    #f = int((1 / (sqrt(5))) * pow(pow(((1 + sqrt(5)) / 2), num) - (((1 - sqrt(5))) / 2), num))

    f = pow(((1+(sqrt(5)))/2),num)
    f = f - pow(((1-sqrt(5))/2),num)
    f = f * 1/(sqrt(5))
    return int(f)

num = 1
print("programa que implementalas 3 variantes para calcular fibonacci")
while num != 0:
    print("* ingrese un 0 para terminar el programa")
    num = int(input("ingrese un numero para calcular la succession:"))
    if num != 0:
        print("-----------------------")
        t1_start = perf_counter()
        print("fibo iterativo", fibo_iter(num))
        t1_stop = perf_counter()
        print("el tiempo transcurrido de forma iterativa fue de:{} s".format(round((t1_stop - t1_start), 7)))
        print("-----------------------")
        try:
            t1_start = perf_counter()
            print("fibo formula:", fibo_formula(num))
            t1_stop = perf_counter()
            print("el timepor transcurrido utilizando la formula fue de:{} s".format(round((t1_stop - t1_start), 10)))
        except OverflowError:
            print("Overflow al hacer el calculo con la formula")
        print("-----------------------")
        try:
            t1_start = perf_counter()
            print("el res es:", fibo_recu(num))
            t1_stop = perf_counter()
            print("el timepor transcurrido de forma recursiva fue de:{}s".format(round((t1_stop - t1_start), 7)))
            print("-----------------------")
        except RecursionError:
            print("El recursivo llego al maximo de la pila y se desbordo :(")
    else:
        print("Saliendo...")
