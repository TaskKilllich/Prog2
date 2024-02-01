"""Ejercicio 9
Escriba un método espejo() para extender el TAD Cola, que agregue los elementos al final de la cola en orden
inverso, formando una cola “capicúa”.
Resuelva y calcule el orden de complejidad de la función espejo() resultante.
Ejemplos: a l → a l l a
1 123 casa ( → 1 123 casa ( ( casa 123 1
Juan Ana Paula → Juan Ana Paula Paula Ana Juan"""

from Cola import *

def mirror():
    print(new_cola.elementos)
    cola_capi = new_cola.espejar()
    print(cola_capi)
    return 0

cadena = 0
new_cola = Cola()
print("ingrese un * para terminar")
while cadena != '*':
    cadena = input("elemento:")
    if cadena != '*':
        new_cola.encolar(cadena)
    else:
        print("-----------------")


mirror()

