"""Ejercicio 3
A partir del ejercicio anterior, diseñar una función recursiva que, dados a y b, calcule:"""


def sumatoria_de_a_a_b(a,b):
    if b == a:
        return 1
    else:
        return b + sumatoria_de_a_a_b(a, b-1)

num1 = 1
num2 = 1
while num1 != 0 and num2 != 0:
    print("---------------------------------------------")
    print("** ingrese un 0 en cualquier momento para salir")
    print("calcular la sumatoria desde un valor a otro")
    num1 = int(input("ingrese su primer valor:"))
    if num1 != 0:
        num2 = int(input("ingrese su segundo valor:"))
        if num2 != 0:
            a = min(num1,num2)
            b = max(num1,num2)
            print("la sumatoria de {} hasta {} es:".format(a,b))
            print(sumatoria_de_a_a_b(a,b))
        else:
            print("Saliendo")
    else:
        print("Saliendo")
