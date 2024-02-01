"""Ejercicio 4
Escribir un programa que implemente un algoritmo RECURSIVO para determinar el número de bits necesarios
para representar un entero sin signo dado."""

def num_bits(entero):
    if entero<=1:
        return 1
    else:
        return 1+num_bits(entero//2)



print("determinar el numero de bits necesarios para reprecentar un entero sin signo")
terminar = False
while terminar == False:
    print("----------------------------------")
    try:
        print("**ingrese un 0 para terminar**")
        entero = int(input("ingrese su entero:"))
        if entero < 0:
            entero = entero * -1
        else:
            print("se necesitan {} bits para reprecentar un {}".format(num_bits(entero),entero))
        if entero == 0:
            terminar = True
            print("Saliendo...")

    except ValueError:
        print("Error: ingrese un valor entero")


