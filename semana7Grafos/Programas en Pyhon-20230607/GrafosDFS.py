from ClaseGrafo import *

def procesar_vertice_temprano(valor_vertice):
    print("Vértice ", valor_vertice)

def procesar_vertice_tarde(valor_vertice):
    return None

def DFS_recursivo(G, s, estado, padre):
    
    if estado[s] == "V":
        return
    procesar_vertice_temprano(s)
    estado[s] = "V"
    adyacente = G.primer_adyacente(s)
    while adyacente:
        valor = adyacente.valor()
        if estado[valor] == "N":
            padre[valor] = s
            DFS_recursivo(G, valor, estado, padre)
        adyacente = adyacente.proximo()
           
    procesar_vertice_tarde(s)
        
def DFS(G, s):

    estado = {}
    padre = {}

    """ Inicializar el diccionario de estados y de padres"""
    vertices = G.vertices()
    for ve in vertices:
        estado[ve]= "N"
        padre[ve] = None

    DFS_recursivo(G, s, estado, padre)
    
    """ Devolver el diccionario de padres!! """
    """ Para armar el árbol resultante """
    return padre

