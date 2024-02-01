"""Ejercicio 1
La siguiente función implementa recursivamente una comparación entre dos números naturales. ¿Cuál es esa
comparación? Escribir el enunciado correspondiente, algo así como: “Escriba una función recursiva que, dados
dos números enteros a y b, …...” y corregir el nombre de la función, eligiendo un nombre adecuado según las
reglas del código autodocumentado"""

"""Escribir un programa que pida dos numeros enteros y calcule de forma recursiva cual de ellos es mayor"""

def Mayor_entre(a,b):
    if b == 0:
        return False
    elif a==0:
        return True
    else:
        return Mayor_entre(a-1,b-1)


print("programa que compara recursivamente el menor enrte dos numeros")

terminar = False
while terminar == False:
    a = int(input("num1 :"))
    b = int(input("num2 :"))
    res = Mayor_entre(a,b)
    if res is True:
        print("El segundo numero es Mayor al primer numero ingresado")

    else:
        print("El primer numero es Mayor al segundo numero ingresado")

    op = input("comparar otro par de numeros? (s/n):")
    op = op.lower()
    if op == 'n':
        print("Saliendo...")
