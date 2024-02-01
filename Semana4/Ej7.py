"""Ejercicio 7
En la siguiente secuencia, una letra significa encolar() y un asterisco, desencolar(). Mostrar la secuencia de
valores que devuelve el método desencolar() para todos los elementos restantes de la cola, una vez que se aplicó
la secuencia de operaciones a una cola vacía.
(a) C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * * D E L B A Ñ O * * * * * *
(b) P A * S O P * * O * R T * U C * * A S * A *"""
from Cola import *

new_cola = Cola()
new_cola_b = Cola()
string_a = 'C A Y * * O P O * * R L * A * * V E N T * * * I L * A C * I O * * * N * * D E L B A Ñ O * * * * * *'
string_b = "P A * S O P * * O * R T * U C * * A S * A *"
string_a = string_a.split()
string_b = string_b.split()
for i in string_a:
    if i == '*':
        print('saco:',new_cola.desencolar())
    else:
        new_cola.encolar(i)
        print('encolo:',i)

for i in string_b:
    if i == "*":
        new_cola_b.desencolar()
    else:
        new_cola_b.encolar(i)

print("cadenas originales:")
print('a)',''.join(string_a))
print('b)',''.join(string_b))
print("contenido de las colas si las letras apilan y los * desapilan")
print(new_cola.elementos)
print(new_cola_b.elementos)

print("lo que sucede es: se encolan  las primeras tres letras 'C,A,Y' y los sigientes 2 asteriscos desencolan lo que esta al principio de la cola\nse desencola la C y la A")
print("se encola 'O,P,O' y los siguientes dos * desencolan la 'Y', 'O' y asi. encolo R, L. Saco P. encolo A. Saco O, R")
print("cada asterisco va desencolando desde el principio de la cola")
print("si se quisiera desencolar el resultado para imprimirlo se desencolaria primor la B luego la A -> Ñ -> O")
print("\n")
print("Lo mismo para la cadena b)")
print("se encola P,A. se desencola P. se encola S,O,P. se desencola A, S. cada asterisco desencola desde el principio de la cola.")


