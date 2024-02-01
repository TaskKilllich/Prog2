"""Ejercicio 1
Una letra significa apilar() y un asterisco, desapilar() en la siguiente secuencia. Si se parte de una estructura vacía,
¿cómo quedará la pila luego de aplicar dicha secuencia? Y si desapilamos los valores que quedan, cuales son las
cadenas de caracteres que se forman?
(a) E * S U N * * A * P I Ñ * * * A , * P A * T * O
(b) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * *"""

from Pila import *

def convertir_a_rpn(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    pila = Pila()
    salida = []

    for i in expresion:
        if i.isdigit():

            salida.append(i)
        elif i in precedencia:
            #para que quede bien la procedencia
            while not pila.esta_vacia() and pila.ver_tope() in precedencia and precedencia[i] <= precedencia[pila.ver_tope()]:
                salida.append(pila.desapilar())
            pila.apilar(i)

        elif i == '(':
            pila.apilar(i)

        elif i == ')':

            while not pila.esta_vacia() and pila.ver_tope() != '(':
                salida.append(pila.desapilar())
            if not pila.esta_vacia() and pila.ver_tope() == '(':
                pila.desapilar()

    # Vaciar la pila a la salida
    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    expresion_rpn = ''.join(salida)
    if '--' in expresion_rpn or '++' in expresion_rpn or '+-' in expresion_rpn or '-+' in expresion_rpn:
        raise ValueError("Expresión inválida: signos duplicados")

    return salida

