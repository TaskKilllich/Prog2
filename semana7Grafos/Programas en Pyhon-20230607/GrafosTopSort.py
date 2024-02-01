from ClaseGrafo import *

def procesar_vertice_tarde(valor_vertice):
    print("Vértice ", valor_vertice)

def tophelp(G, s, estado):
    
#    if estado[s] == "V":
#        return
    estado[s] = "V"
    adyacente = G.primer_adyacente(s)
    while adyacente:
        valor = adyacente.valor()
        if estado[valor] == "N":
            tophelp(G, valor, estado)
        adyacente = adyacente.proximo()
           
    procesar_vertice_tarde(s)

def TopSort(G):

    estado = {}
  
    """ Inicializar el diccionario de estados"""
    vertices = G.vertices()
    for ve in vertices:
        estado[ve]= "N"

    """ Recorro todos los vértices del grafo,
    descartando aquellos que ya visitamos """
    for ve in vertices:
        if estado[ve] == "N":
            tophelp(G, ve, estado)
        
    
  

