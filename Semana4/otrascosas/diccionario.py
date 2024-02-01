from Pila import *

Diccionario = {'if001':Pila(),
               'if002':Pila()}
#x = input("ingrese clave")
#print(Diccionario.keys())
#a=Diccionario.pop('if001')  #remueve clave y valor del diccionario

#print(Diccionario.keys())
for i in range(10):
    Diccionario.get('if001').push(i)
    Diccionario.get('if002').push(i-2)


print(Diccionario.get('if001').elementos)
print(Diccionario.get('if002').elementos)