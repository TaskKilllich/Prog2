"""Ejercicio 6
a. Escribir un programa que calcule el máximo común divisor (mcd) de dos números n y m, utilizando el algoritmo
de Euclides, un método que se conoce desde la antigüedad y que se suele considerar el primer algoritmo
propuesto por el hombre. El algoritmo dice así:
Calcula el resto de dividir el mayor de los dos números por el menor de ellos. Si el resto es cero,
entonces el máximo común divisor es el menor de ambos números. Si el resto es distinto de cero, el
máximo común divisor de n y m es el máximo común divisor de otro par de números: el formado por
el menor de n y m y por dicho resto. (Para calcular el resto, se puede utilizar el operador %)
b. Hacer una traza de las llamadas a mcd para los números 1847 y 1106."""


"""mcd(55,10)
    55 / 10  = resto 5
    si es distinto de 0,
    el maximo es  otro par de numeros conformados por 
    (10 , 5)  = resto 0
    como resto 0, el mcd es el menor entre los dos numeros anteriores    
"""


def mcd(n,m):
    if n%m == 0:
        return min(n,m)
    else:
        return mcd(n=m,m=n%m)


print("programa que calcula el maximo comun divisor entre dos numeros")

n = int(input("ingrese su primer numero:"))
m = int(input("ingrese el segundo numero:"))


print ("el maximo comun divisor es:",mcd(n,m))



