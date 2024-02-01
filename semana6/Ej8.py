"""Ejercicio 8
Implemente, usando el TAD Árbol, un programa que arme el árbol genealógico de una persona, partiendo de esa
persona (raíz) y preguntando quién es su madre/padre. Deberá terminar con una persona cuando la respuesta, en
cada caso, sea “no sé”. Una vez cargado el árbol, imprímalo. Puede usar el módulo que imprime árboles
gráficamente, con las adaptaciones necesarias para que “entren” los nombres."""

from ArbolBB import *
from ImprimirGtreetortuga import *

"""def pedirdatos(persona):
    parte_materna = None
    parte_paterna = None
#de jose
    nom_materno = input(f"Quién es la madre de {persona}: ")
    nom_paterno = input(f"Quién es el padre de {persona}: ")

    if nom_materno.lower() == "n" and nom_paterno.lower() == "n":
        return ArbolBB(persona)

    if nom_materno.lower() != "n":
        parte_materna = pedirdatos(nom_materno)

    if nom_paterno.lower() != "n":
        parte_paterna = pedirdatos(nom_paterno)

    return ArbolBB(persona, parte_materna, parte_paterna)
"""
def pedirdatos():
    print("*Si no conoce el nombre de algun familiar ponga no se o presione enter")
    arbol_genealogico(famili_tree)
    return

print("-- Arbol Genealogico --")
su_nombre = input("Ingrese su nombre:")
su_nombre = su_nombre.capitalize()
#famili_tree = pedirdatos(su_nombre)
famili_tree = ArbolBB(su_nombre)
pedirdatos()
ImprimirABT(famili_tree)
turtle.done()









