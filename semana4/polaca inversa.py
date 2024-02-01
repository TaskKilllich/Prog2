"""Ejercicio 1
Una letra significa apilar() y un asterisco, desapilar() en la siguiente secuencia. Si se parte de una estructura vacía,
¿cómo quedará la pila luego de aplicar dicha secuencia? Y si desapilamos los valores que quedan, cuales son las
cadenas de caracteres que se forman?
(a) E * S U N * * A * P I Ñ * * * A , * P A * T * O
(b) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * *"""

from Pila import *

def polacainv(expresion):
    operacion = expresion.split()

    operando = '*-+/'
    print(operacion)
    for i in range(len(operacion)):
        print(i,new_pila.elementos)
        if not operacion[i] in operando:
            new_pila.push(operacion[i])
        else:

            n2 = new_pila.pop()
            n1 = new_pila.pop()
            try:
                res = str(eval(n1 + operacion[i] + n2))
                new_pila.push(res)
            except NameError:
                print("se intento hacer la operacion pero fallo el calculo")


new_pila = Pila()
#expresion = "123 47 2 * +"
expresion = input("Ingrese su expresion en notacion polaca inversa   --ej:123 47 2 * + \n**Ingrese un 0 para terminar \nexpresion:")
polacainv(expresion)
print(new_pila.elementos)


'''informar si la pila termina con mas numeros'''

