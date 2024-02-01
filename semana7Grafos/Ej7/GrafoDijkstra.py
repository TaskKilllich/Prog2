from Vertices import *
import numpy as np
class Grafo:
    def __init__(self, es_dirigido=False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido
        self.matriz = []

    def __str__(self):
        return "G = ("+str(self.n_vertices())+" V, "+str(self.n_arcos)+" A)"

    def n_vertices(self):
        return len(self.lista_vertices)

    def dirigido(self):
        return self.es_dirigido

    def n_arcos(self):
        return self.n_arcos

    def matriz_tamanio(self):
        return len(self.matriz)

    def ver_matriz(self):
        return self.matriz

    def vertices(self):
        return self.lista_vertices

    def insertar_conpeso(self, x, z, peso_arco=0, dirigido=True):
        """ Agregar el vértice de origen """
        if x == z:
            print(f"Mismo vertice no admitido:{x,z}")
            return
        if x not in self.lista_vertices:
            self.lista_vertices[x] = None
        """ Agregar el destino (ojo, x sumideros)"""
        if z not in self.lista_vertices:
            self.lista_vertices[z] = None

        nw = Vertice(z, peso_arco, self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos += 1
        if dirigido is False and z != x:
            self.insertar_conpeso(z, x,peso_arco, True)


    def imprimir(self):
        print("vertice -> (destino:distancia)")
        for vertice in self.lista_vertices:
            print(f'   {vertice}', end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print(" ->", end=' ')
                arco.imprimeLista()
            else:
                print("")

    def imprimir_vertices(self):
        for vertice in self.lista_vertices:
            print(vertice, end='')

    def primer_adyacente(self, x):
        """ Devuelve el primer vértice adyacente (si existe) de x"""
        if x not in self.lista_vertices:
            raise Error("El vértice no existe en el diccionario del Grafo")
        else:
            arco = self.lista_vertices[x]

            return self.lista_vertices[x]


def inicializar_v(vertices):
    """ Devuelve una lista c/los vértices sin descubrir """
    """ y en orden. Todos tienen False en el estado """
    visitados = []
    for ve in sorted(vertices.items()):
        elem = list(ve)
        elem[1] = False  # Todos sin descubrir!
        visitados.append(elem)
    return visitados


def set_mark(visitados, ve, valor):
    """ Pone el valor del vértice ve en visitado, ve existe """
    i = 0  # Encontrar el vértice ve
    while (i < len(visitados) and visitados[i][0] != ve):
        i += 1
    visitados[i][1] = valor  # Modificar


def Dijkstra(G, s):
    """ Calcula el menor camino desde s a todos los vértices de G """

    """ Inicializar el diccionario de distancias """
    distancia = {}
    vertices = G.vertices()
    for ve in vertices:
        distancia[ve] = float("inf")  # infinito en Python

    """ Listado de los vértices (ORDENADOS) con visitado = False """
    visitados = inicializar_v(vertices)

    distancia[s] = 0
    while quedan_sin_descubrir(visitados):

        v = minVert(G, distancia, visitados)  # encontrar el próximo mas cercano
        print("Ver:", v)
        set_mark(visitados, v, True)
        if distancia[v] == float("inf"):  # vertice inalcanzable
            print("Componente no conexa: ", v)
        else:
            arista = G.primer_adyacente(v)
            print("primer adyacente: ", arista)
            while arista:
                w = arista.valor()  # devuelve el veŕtice
                if (distancia[w] > (distancia[v] + arista.peso())):
                    distancia[w] = distancia[v] + arista.peso()
                    print(v, w, "d", distancia[w])
                arista = arista.proximo()
    return distancia


def minVert(G, dist, visit):
    """ Encuentra el menor de los no visitados """
    """ Recibe el grafo, el dicc de distancias y la lista de visitados"""

    i = 0
    while i < len(visit) and visit[i][1]:
        i += 1  # Iterar hasta encontrar el primer falso
    if i < len(visit):
        v = visit[i][0]  # Encontré uno sin visitar. Es el mínimo?
        for i in range(i + 1, len(visit)):
            if (visit[i][1] == False and dist[visit[i][0]] < dist[v]):
                v = visit[i][0]  # Hay otro menor
    else:
        v = None  # Puede ser que no haya ninguno?
    return v


def quedan_sin_descubrir(visitados):
    """ Devuelve True/False según queden vértices sin visitar """
    indice = 0
    while indice < len(visitados) and visitados[indice][1]:
        indice += 1
    return (indice < len(visitados) and (not visitados[indice][1]))


