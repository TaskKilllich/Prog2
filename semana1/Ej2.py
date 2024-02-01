"""Ejercicio 2
Escribir un programa que permita evaluar el polinomio x4 + x3 + 2x2 − x. Luego, escribir otro programa que solicite
valores de x por teclado y calcule el valor del polinomio para ellos, mostrando el resultado. Es importante tener en
cuenta cuál es la modularización adecuada del problema y cuál sería el criterio de parada al ingreso de datos."""



def solicitar_valores():
    x=[]
    print("ingrese valores que quiere que tome la variable x")
    print("ingrese un '*' para terminar de cargar")
    i=1
    numero = 0
    while numero != '*':
        numero = input("x{} = ".format(i))
        if numero != '*':
            try:
                numero = float(numero)            #se convierte a entero porque sino los toma como str
                x.append(numero)
                i += 1
            except ValueError:
                print("--Error: intente nuevamente")

    return x

def evaluar(x):
    res = []
    for i in range(0,len(x)):
        aux = x[i]**4+x[i]**3+2*x[i]**2-x[i]
        res.append(aux)
    return res


terminar = False

print("--------------------------------------------------------------------------------")
print("programa que evalua el polinomio x^4 + x^3 + 2x^2 − x  para cierto valor de x")
print("--------------------------------------------------------------------------------")
while terminar == False:
    x=solicitar_valores()
    res=evaluar(x)
    print("para el polinomio: x^4 + x^3 + 2x^2 − x  el resultado para los distintos valores de x es:")
    print("-----------------------")
    for i in range(0,len(x)):
        print("P({}) = {}".format(x[i],res[i]))
    print("-----------------------")
    op = input("\ndesea evaluar para otro x? (y/n) :")

    if op == 'n':
        terminar = True