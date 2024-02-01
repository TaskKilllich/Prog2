"""Ejercicio 1
Una letra significa apilar() y un asterisco, desapilar() en la siguiente secuencia. Si se parte de una estructura vacía,
¿cómo quedará la pila luego de aplicar dicha secuencia? Y si desapilamos los valores que quedan, cuales son las
cadenas de caracteres que se forman?
(a) E * S U N * * A * P I Ñ * * * A , * P A * T * O
(b) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * """
"""covide"""
from Pila import *

def apiladesapila(cadena1,cadena2):
    for i in cadena1:
        if i != '*':
            new_pila.push(i)
        else:
            new_pila.pop()

    for i in cadena2:
        if i != '*':
            new_pila2.push(i)
        else:
            new_pila2.pop()
    return 0

new_pila = Pila()
new_pila2 = Pila()
print("una letra significa apilar y un asterisco significa desapilar ")
cadena1 = 'E * S U N * * A * P I Ñ * * * A , * P A * T * O'
cadena2 = 'C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * * '
cadena1 = cadena1.split()
cadena2 = cadena2.split()
apiladesapila(cadena1,cadena2)
cad1 = ''.join(new_pila.elementos)
cad2 = ''.join(new_pila2.elementos)
print("cadena1 = E * S U N * * A * P I Ñ * * * A , * P A * T * O\nsi se desapila segun al condicion queda:{}\n-----------------------------\ncadena2=C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * D E L B A Ñ O * * * * *\nsi se desapila segun al condicion queda:{}".format(cad1,cad2))
print("Los asteriscos van desapilando las ultimas letras que se apilaron")


