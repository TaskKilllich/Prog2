"""Ejercicio 4
Diseñar una función que reciba los tres coeficientes de una ecuación de segundo grado, y devuelva una lista con
sus soluciones reales.     Ecuación de 2º grado: ax^2 + bx + c = 0
Si la ecuación sólo tiene una solución real, devuelve una lista con dos copias de la misma. Si no tiene solución real
alguna o si tiene infinitas soluciones, devuelve una lista con dos copias del valor None."""

from math import sqrt
def bhaskara(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        print("no hay soluciones reales, hay soluciones complejas")
        delta = delta *-1       #la raiz de un numero negativo es imaginaria
        x1 = (-b)/(2*a)
        x2 = sqrt(delta)/(2*a)
        return x1,x2,"i"
    elif delta == 0:
        return 0
    else:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        return x1,x2


print("calculo de Ecuación de 2º grado")
terminar = False
while terminar == False:
    print("--------------------------------------")
    print("ingrese el valor de sus coeficinetes...")
    print("--------------------------------------")
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    if a == 0:
        print("No es una ecuación de segundo grado porque el coeficiente de x2 es a = 0.")
    else:
        print("el resultado de la ecuacion es:",bhaskara(a,b,c))
    print("--------------------------------------")
    op = input("calcular otro numero? y/n :")
    op = op.lower()
    if op == "n":
        terminar = True


