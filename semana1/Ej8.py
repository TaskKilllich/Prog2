"""Ejercicio 8
Diseñar un programa que lea un texto criptográfico siguiendo la técnica descrita en el ejercicio anterior y el valor
de n utilizado al encriptar para mostrar ahora el texto decodificado."""

def desencriptar(texto,n):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    encript=''
    for letra in texto:
        if letra in abc:
            pos = abc.index(letra)

            encript = encript + abc[(pos-n)%len(abc)]  #si tengo que intercambiar por una pos que esta fuera del rango del arreglo (pos+n)%len(abc) soluciona
                            #ya que al hacer 1 pos mas 26%26 =0 vuelve a la posicion 0 y si me quiero mover por ej 4 a partir de z 29%26 = 3 z->d
        elif letra in ABC:
            pos = ABC.index(letra)

            encript = encript + ABC[(pos - n) % len(ABC)]
        else:
            encript = encript + letra

    return encript

print("desencriptar texto")
print("**el desencriptar no reconoce numeros o acentos**")
print("----------------------------------------")
texto = input("ingrese su texto codificado:")
n = int(input("ingrese la base en la que esta codificado:"))

print(desencriptar(texto,n))
