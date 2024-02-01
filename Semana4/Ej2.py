"""Ejercicio 2
Implementar una función que, usando el TAD Pila, devuelva una nueva pila invertida. Es decir que el elemento que
estaba en el tope de la pila original, ahora estará abajo de todo."""


from Pila import *


def invertirpila():
    pila_invertida = Pila()
    for i in pila_original.elementos[::-1]:  #leo la pila al revez y voy apilando de forma que los elementos que estaban arriba de la pila quedaran abajo
        pila_invertida.push(i)                  #tambien se podria hacer desapilando la pilaoriginal y apilando en la pila invertida, pero eso dejaria sin elementos a la pila original
    return pila_invertida

pila_original = Pila()

posiciones = ['primera','segunda','tercera','cuarta','quinta','sexta','septima','octava','novena']

for i in posiciones:
    pila_original.push(i)

print("pila original:",pila_original.elementos)
pila_invertida = invertirpila()
print("pila invertida:",pila_invertida.elementos)




