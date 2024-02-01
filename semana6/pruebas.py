"""def cargararbol():
    lista_num = []
    l_operando = []
    aux_oper = ''
    operacion = input("operacion:")
    for i in operacion:
        if i.isdigit():
            aux_oper += i
        else:
            lista_num.append(aux_oper)
            l_operando.append(i)
            aux_oper = ''
    lista_num.append(aux_oper)
    new_arbol = ArbolBE(l_operando[0])
    j=1
    for i in range(len(lista_num)):
        new_arbol.insertar(lista_num[i])
        if j<i:
            new_arbol.insertar(l_operando[j])
        j+=1
    print(lista_num)
    print(l_operando)
    if '' in lista_num:
        print("mal formulada la operacion")
    ImprimirABT(new_arbol)
    turtle.done()
    return

new_arbol = cargararbol()"""
import turtle

from ArbolBE import *
from random import randrange
from ImprimirABBtortuga import *
from ArbolBB import *
"""new_arbol = ArbolBE()
for i in range(randrange(8,9)):
    new_arbol.insertar(randrange(0,50))
new_arbol.imprimir()"""

"""


def coso():
    famili = {1: ['Abuela', 'Abuelo'],
              2: ['Bisabuela', 'Bisabuelo'],
              4: ['Tatarabuela', 'Tatarabuelo'],
              8: ['Trastataraabuela', 'Trastataraabuelo'],
              16: ['Pentaabuela', 'Pentabuelo']}

    lista_nombres = ['mama','papa','abuelamat','abuelomat','abuelapat','abuelopat','bisamat','bisomat','bisamat','bisomat','bisapat','bisopat','bisapat','bisopat']
    lista_materna = ['mama','abuelamat','abuelomat','bisamat','bisomat','bisamat','bisomat',]
    lista_paterna = ['papa','abuelapat','abuelopat','bisapat','bisopat','bisapat','bisopat']
    lista_otra = ['mama','papa','abuelamat','abuelomat','bisamat','bisomat','bisamat','bisomat','abuelapat','abuelopat','bisapat','bisopat','bisapat','bisopat']
    lista_asd = ['mama','papa','abuelamat','abuelapat','abuelomat','abuelopat','bisamat1','bisapat1','bisomat2','bisopat2','bisamat3','bisapat3','bisomat4','bisopat4']

    lista = ['1', '1', '2m1', '2p1', '2m2', '2p2', '1', '5', '3', '8', '2', '4', '7', '6']
    lista = {50:'mama', 75:'abuelamat', 150:'abuelomat',  10:'abuelopat', 30:'bisamat', 60:'bisomat', 85:'bisapat', 125:'bisopat', 170:'bisapat', 225:'bisopat', 300:'bisopat'}
    new_arbol = ArbolBB(100)

    for key,i in lista.items():
       new_arbol.insertar(key)


    ImprimirABT(new_arbol)
    turtle.done()

coso()
famili = {
    2: ['Abuela', 'Abuelo'],
    4: ['Bisabuela', 'Bisabuelo'],
    8: ['Tatarabuela', 'Tatarabuelo'],
    16: ['Trastataraabuela', 'Trastataraabuelo'],
    32: ['Pentaabuela', 'Pentabuelo']
}
"""
def construirArbolGenealogicoIterativo(persona):
    madre = input(f"¿Quién es la madre de {persona}? (Escribe 'no sé' si no sabes): ")
    padre = input(f"¿Quién es el padre de {persona}? (Escribe 'no sé' si no sabes): ")

    if madre.lower() == "no sé" and padre.lower() == "no sé":
        return ArbolBB(persona)

    arbolMadre = None
    arbolPadre = None

    if madre.lower() != "no sé":
        arbolMadre = ArbolBB(madre)

    if padre.lower() != "no sé":
        arbolPadre = ArbolBB(padre)

    arbolActual = ArbolBB(persona, arbolMadre, arbolPadre)
    arbolesPendientes = [arbolActual]

    while arbolesPendientes:
        arbolActual = arbolesPendientes.pop(0)
        personaActual = arbolActual.persona

        madre = input(f"¿Quién es la madre de {personaActual}? (Escribe 'no sé' si no sabes): ")
        padre = input(f"¿Quién es el padre de {personaActual}? (Escribe 'no sé' si no sabes): ")

        if madre.lower() != "no sé":
            arbolMadre = ArbolBB(madre)
            arbolActual.arbolMadre = arbolMadre
            arbolesPendientes.append(arbolMadre)

        if padre.lower() != "no sé":
            arbolPadre = ArbolBB(padre)
            arbolActual.arbolPadre = arbolPadre
            arbolesPendientes.append(arbolPadre)

    return arbolActual

new_arbol = construirArbolGenealogicoIterativo('Aaron')
ImprimirABT(new_arbol)