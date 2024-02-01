"""Ejercicio 5
Diseñar y escribir una función que determine si un número natural (entero mayor que 1) es o no primo.
Luego escribir el programa que lea un número ingresado por teclado y, utilizando la función previamente escrita,
determine si es primo o no. El algoritmo deberá continuar pidiendo números, hasta que el usuario ingrese un
número 0. En ese caso, se debe confirmar la salida del programa, dando al usuario la posibilidad de seguir
ingresando números."""

def primo(num):
    esprimo = 0
    if num == 1:
        return 0       #uno no es primo
    else:
        for i in range(1,num+1):
            if num%i == 0:         #si el resto de la divicion es 0 enrta
                esprimo+=1
                if esprimo >2:       #si entro mas de 2 veces no hace falta que termine de comprobar con
                    return 0         #todo el resto de numeros
        return 1

print("-----------------------------------------")
print("determinar si un numero natural es o no primo")
num = -1
while num != 0:
    print("-----------------------------------------")
    print("*ingrese un 0 para salir")
    try:
        num = int(input("ingrese su numero:"))
        if num < 0 :
            print("Un numero negativo no puede ser primo por definicion")
        else:
            if num != 0:
                esprimo=primo(num)
                if esprimo == 1:
                    print("el numero {} es primo".format(num))
                else:
                    print("el numero {} NO es primo".format(num))
    except ValueError:
        print("--Error: asegurese de ingresar un numero entero positivo, intente nuevamente...")
print("saliendo...")

