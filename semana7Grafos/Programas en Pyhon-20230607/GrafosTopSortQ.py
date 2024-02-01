from ClaseGrafo import *
from ClaseCola import *

def procesar_vertice_temprano(valor_vertice):
    print("Vértice ", valor_vertice)

def TopSortQ(G):

    q_vert = Cola()
    cuenta = {}
  
    """ Inicializar el diccionario de requisitos """
    vertices = G.vertices()
    for ve in vertices:
        cuenta[ve]= 0

    """ Recorro todos los vértices del grafo,
    para procesar las aristas """
    for ve in vertices:
        adyacente = G.primer_adyacente(ve)
        while adyacente:
            valor = adyacente.valor()
            cuenta[valor] += 1
            adyacente = adyacente.proximo()        

    for ve in cuenta:
        if cuenta[ve] == 0:
            """ ve no tiene requisitos, se puede procesar """
            q_vert.encolar(ve)
            
    while not q_vert.esta_vacia():
        ve = q_vert.desencolar()
        procesar_vertice_temprano(ve)
        
        adyacente = G.primer_adyacente(ve)
        while adyacente:
            valor = adyacente.valor()
            cuenta[valor] -= 1
            if cuenta[valor] == 0:
                """ el vértice fue liberado """
                q_vert.encolar(valor)
            
            adyacente = adyacente.proximo()


