"""Ejercicio 6
Una palabra es alfabética si todas sus letras están ordenadas alfabéticamente. Por ejemplo: amor, chino e himno
son palabras alfabéticas. Diseñar un programa que lea una palabra y nos diga si es alfabética o no."""

def alfabetica(palabra):

    for i in range(0,len(palabra)-1):  # una letra menos para que no se salga del rango
        if palabra[i] > palabra[i+1]:
            return 0
    return 1

print("analizar si una palabra es Alfabetica *si las letras de la palabra estan ordenadas, la palabra sera alfabetica")
palabra = 'a'
while palabra != '*':
    print("--------------------------------------------------")
    print("ingrese un * para terminar")
    palabra = input("Ingrese su palabra:")
    if palabra != '*':
        if len(palabra) <= 1:
            print("No hay letras con la cual comparar...")
        else:
            if alfabetica(palabra) == 0:
                print("Su palabra {} No es alfabetica".format(palabra))
            else:
                print("Su palabra {} Es alfabetica".format(palabra))
print("saliendo...")