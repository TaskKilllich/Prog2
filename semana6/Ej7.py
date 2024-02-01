"""Ejercicio 7
Escriba un programa que reciba una operación matemática, del tipo: 3+4*(6/7), en formato string, y que la cargue
en un árbol de expresión y devuelva el resultado de dicha expresión. Para esto, deberá agregar a la clase Árbol de
Expresión un método recursivo, llamado Evaluar."""

from ArbolBE import *
from ImprimirABBtortuga import *

def separarenterminos(operacion):
    lista_operacion = []
    operandos = '+-/*)('
    aux_oper = ''
    alpha = False
    for i in operacion:
        if i.isdigit():
            aux_oper += i
        elif i.isalpha():
            alpha = True
        else:
            if i in operandos:
                if aux_oper != '':
                    lista_operacion.append(aux_oper)
                lista_operacion.append(i)
            aux_oper = ''

    if aux_oper != '':
        lista_operacion.append(aux_oper)
    if alpha == True:
        print("El string que ingreso tenia caracteres alfabeticos, fueron eliminados")

    return lista_operacion

#por evaluar entendi que se referia a si la operacion estaba bien formada, convierdo la operacione en un rpn y evaluo como vimos en clase
#si se me da el okey de que esta bien formada, paso a costruir el arbol y mostrar el resultado

terminar = False
while terminar == False:
    operacion = input("operacion:")
    new_arbol = ArbolBE()
    lista_num = separarenterminos(operacion)
    validacion, polaca = new_arbol.evaluar(lista_num)

    if validacion:
        print('se construye el Arbol de expresion a partir de la polaca inversa:',polaca)
        new_arbol = construir_arbole(polaca)
        new_arbol.imprimir()
        print("es una operacion valida")
        print(f'{operacion}={eval(operacion)}')
        new_arbol.resultado()

        ImprimirABT(new_arbol)
        turtle.done()
    else:
        print("no es una operacion valida")
    op = input("hacer otra operacion?(s/n)")
    if op.lower() == 'n':
        print("Saliendo")

#queriaa usar a toda costa el polaco inverso