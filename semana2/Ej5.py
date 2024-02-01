"""Ejercicio 5
Suponiendo que la función del Ejercicio 4 se llame cuantos_bits(n), dibujar el árbol de llamadas que muestre paso
a paso lo que ocurre al calcular cuantos_bits(63), incluyendo los valores que devuelve cada llamada a la función."""


"""hacer dibujo"""

def num_bits(entero,slot):
    if entero<=1:
        print("\n------- ultima llamada *caso base-------")
        print("num_bits({}) = 1 + num_bits({}//2)".format(entero, entero))
        print("se agrego {} bit".format(slot))
        return 1

    else:
        print("------- llamada {} -------".format(slot))
        print("num_bits({}) = 1 + num_bits({}//2)".format(entero,entero//2))
        print("se agrego {} bit".format(slot))

        return 1+num_bits(entero//2,slot+1)

print("determinar el numero de bits necesarios para reprecentar un entero sin signo")

entero = int(input("ingrese su entero:"))
slot = 1
print("\nse necesitan {} bits para reprecentar un {}".format(num_bits(entero,slot),entero))




