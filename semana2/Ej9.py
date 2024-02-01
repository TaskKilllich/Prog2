"""Ejercicio 9
Escriba un algoritmo para calcular los números combinatorios en forma recursiva, sabiendo que: formula de
combinatoria y el combinatorio de dos numeros iguales o el combinatorio de un numero con 0 es = 1"""


def combinatorio(n,m):
    if n == m or m==0:
        return 1
    return combinatorio(n-1,m) + combinatorio(n-1,m-1)


print("Calcular el combinatorio nCr([n],[m])")
terminar = False
while terminar == False:
    print("------------------------------------------------------")
    try:
        n = int(input("n:"))
        m = int (input("m:"))
        if n<0 or m<0:
            print("No se puede calcular el combinatorio de numeros negativos, intente nuevamente...")
        elif min(n,m) == n and n != m:
            print("Error: n tiene que ser mayor a m, intente nuevamente...")
        else:
            print("el combinatorio nCr({},{}) = {}".format(n,m,combinatorio(n,m)))
            print("------------------------------------------------------")
            op = input("calcular el combinatorio de otro numero? (s/n)")
            op = op.lower()
            if op == 'n':
                terminar = True
    except ValueError:
        print("Error: valor no valido, intente nuevamente...")



