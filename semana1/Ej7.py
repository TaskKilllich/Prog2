"""Ejercicio 7
Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres del alfabeto
por otro situado n posiciones más a la derecha. Si n = 2, por ejemplo, sustituiremos la a por la c, la b por la d, y así
sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la
letra y se sustituirá por la a y la letra z por la b. La sustitución debe aplicarse a las letras minúsculas y mayúsculas
y a los dígitos. bien 
Diseñar un programa que lea un texto y el valor de n y muestre su versión criptográfica."""


def encriptar(texto,n):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    encript =''
    for letra in texto:
        if letra in abc:
            pos = abc.index(letra)   #index mustra pos
            #print("{}+{}={}   {}+{}%{}={}".format(pos,n,pos+n,pos,n,len(abc),(pos+n)%len(abc)))    #prueba de valores que toma la formula
            encript = encript + abc[(pos+n)%len(abc)]  #si tengo que intercambiar por una pos que esta fuera del rango del arreglo (pos+n)%len(abc) soluciona
                            #ya que al hacer 1 pos mas 26%26 =0 vuelve a la posicion 0 y si me quiero mover por ej 4 a partir de z 29%26 = 3 z->d
        elif letra in ABC:
            pos = ABC.index(letra)
            #print("{}+{}={}   {}+{}%{}={}".format(pos, n, pos + n, pos, n, len(abc),(pos + n) % len(ABC)))
            encript = encript + ABC[(pos + n) % len(ABC)]
        elif letra in digitos:
            pos  = digitos.index(letra)
            encript = encript + digitos[(pos + n) % len(ABC)]
        else:
            encript = encript + letra

    return encript

print("---encriptar texto---")
print("**el encriptador no tiene en cuenta los acentos o simbolos**")
print("----------------------------------------")
texto = input("ingrese su texto:")
n = int(input("ingrese un numero para encriptarlo:"))

print("Su texto {} encriptado es:{}".format(texto,encriptar(texto,n)))



