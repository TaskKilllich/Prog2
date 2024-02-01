"""Ejercicio 1
Diseñar un programa que, dados dos números enteros, muestre por pantalla uno de los siguientes mensajes,
dependiendo de la verificación de la condición que corresponda.
• El segundo es el cuadrado exacto del primero.
• El segundo es menor que el cuadrado del primero.
• El segundo es mayor que el cuadrado del primero"""


def analizador(num1,num2):
    if num2**2 == num1:
        res = "El segundo es el cuadrado exacto del primero.\n"

    elif num2 < num1**2:
        res = "El segundo es menor que el cuadrado del primero.\n"
    
    else:
        res = "El segundo es mayor que el cuadrado del primero.\n"
    return res


terminar = False

while terminar == False:
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("ingrese dos numeros enteros para analizarlos:")
    print("ingrese un * para terminar")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    num1 = input("primer Numero:")
    if num1 == '*':
        terminar = True
        print("Saliendo...")
    else:
        num2 = input("segundo Numero:")
        if num2 == '*':
            terminar = True
            print("Saliendo...")
        else:
            try:
                num1= int(num1)
                num2= int(num2)
                print(analizador(num1, num2))
            except ValueError:
                print("\n--Error: a ingresado algo distinto a un numero entero, intente nuevamente")

