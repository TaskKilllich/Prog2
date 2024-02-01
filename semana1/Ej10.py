"""Ejercicio 10
Diseñar una función que, dada una lista de nombres y una letra, devuelva una lista con todos los nombres que
empiezan por dicha letra."""

def pedirnom():
    listanom = []
    nombre = ''
    print("Para terminar la carga ingrese un *")
    print("-----------------------------------")
    i=1
    while nombre != '*':
        nombre = input("Nombre{}:".format(i))
        if nombre != '*':
            nombre = nombre.capitalize()  #hace la primer letra mayuscula y el resto minuscula por si se ingreso distinto
            listanom.append(nombre)
            i+=1
    return listanom

def devolver(listanom,letra):
    letra = letra.upper()
    encontrado = False
    for i in range(0,len(listanom)):
        if letra == listanom[i][0]:
            print(listanom[i])
            encontrado = True
    if encontrado == False:
        print("No se encotraron nombres con la letra {}".format(letra))

terminar = False
print("ingrese su lista de nombres")
listnom=pedirnom()
while terminar == False:
    letra = input("Para que letra quiere buscar nombres?:")
    print("------------------------------------")
    devolver(listnom,letra)
    print("------------------------------------")
    op = input("Buscar nombres por otra letra?(s/n) :")
    if op == 'n' or op == 'N':
        terminar = True
        print("Saliendo...")



