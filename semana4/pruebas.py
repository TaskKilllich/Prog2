# Definir una lista vacía para almacenar los caracteres
caracteres = []

# Pedir al usuario que ingrese los caracteres
while True:
    caracter = input("Ingrese un caracter (o presione Enter para terminar): ")
    if not caracter:
        break
    caracteres.append(caracter)

# Imprimir la secuencia ingresada y la secuencia inversa
print("Secuencia ingresada: ", end="")
for caracter in caracteres:
    print(caracter, end=" ")
print("\nSecuencia inversa: ", end="")
for caracter in reversed(caracteres):
    print(caracter, end=" ")

# Buscar la posición de la primera 's' y la primera 'a'
posicion_s = None
posicion_a = None
for i in range(len(caracteres)):
    if caracteres[i] == 's' and not posicion_s:
        posicion_s = i
    elif caracteres[i] == 'a' and not posicion_a:
        posicion_a = i
    if posicion_s and posicion_a:
        break

# Imprimir los caracteres desde la primera 'a' hasta la primera 's'
if posicion_a and posicion_s:
    print("\nCaracteres desde la primera 'a' hasta la primera 's': ", end="")
    if posicion_a < posicion_s:
        for i in range(posicion_a, posicion_s + 1):
            print(caracteres[i], end=" ")
    else:
        for i in range(posicion_s, posicion_a + 1):
            print(caracteres[i], end=" ")