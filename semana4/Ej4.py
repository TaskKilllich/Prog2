"""Ejercicio 4
Escribir un programa que chequee si un string ingresado es un palíndromo o no, usando una pila. Nota: un
palíndromo es una palabra o expresión que se lee igual de izquierda a derecha que de derecha a izquierda.
Ejemplos de palíndromos
Palabras aviva-azuza-Neuquen-sedes-salas.
Frases Ella te da detalle - Isaac no ronca así – Añora la roña - Dábale arroz a la zorra el abad."""

from Pila import *

def palindromo(auxpala):
    palin = True
    for i in auxpala:
        letra = new_pila.pop()
        if letra != i.lower():    #comparo de la primer letra del string con la ultima que entro a la pila,
            palin = False          #asi hasta la ultima letra del string y la primer letra que entro a la pila
    return palin

def armarpila(palabra):

    auxpala = palabra.lower()
    auxpala = auxpala.replace(" ","")   #guardo la palabra en la pila sin espacios ni mayusculas
    for i in auxpala:
        new_pila.push(i)
    return auxpala

new_pila = Pila()
palabra = 1
print("_____________________________________________________________________________________________")
print("Programa que chequea si una palabra ingresada en un palindromo.")
print("Un palindomo es una palabra que se lee igual de ambos lados  ej:aviva-azuza-Neuquen-sedes-salas")
print("             -=ingrese un * para terminar=-")
while palabra != "*":
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    palabra = input("Ingrese su palabra:")
    if palabra != '*':
        auxpala = armarpila(palabra)
        palin = palindromo(auxpala)
        if palin == True:
            print("Su palabra '{}' SI es un palindromo.".format(palabra))
        else:
            print("La palabra '{}' NO es un palindormo.".format(palabra))
    else:
        print('adios...')
