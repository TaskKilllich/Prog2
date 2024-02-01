"""Ejercicio 9
Diseñar una función que reciba una lista de palabras (cadenas) y devuelva, simultáneamente, la primera y la
última palabra según el orden alfabético."""

def primulti(lista):
    enorden = []
    lista = sorted(lista, key=str.lower)  #.lower convierte todo a minusculas antes de comparar
    enorden.append(lista[0])    #la primer palabra de la lista
    enorden.append(lista[-1])    # la ultima
    return enorden


palabra = ''
lista = []
print("programa que analiza una lista de palabras y devuelve la primera y la ultima segun su orden alfabetico")
print("-- para terminar la carga ingrese un * --")
i=1
print("Agregar palabra a la lista...")
while palabra != '*':
    palabra = input("Palabra:".format(i))
    if palabra != '*' and len(palabra) >= 1:
        lista.append(palabra)
enorden = primulti(lista)
print("la primera palabra se: {}   y la ultima: {}".format(enorden[0],enorden[1]))



