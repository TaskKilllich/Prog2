from ClaseListaE import *

def cargar(grafo):
    grafo.insertar("Esquel","Teka")
    grafo.insertar("Teka","Trelew")
    grafo.insertar("Teka", "Sarmiento")

provincia = Grafo()
cargar(provincia)
provincia.imprimir()