from Vertices import *
import numpy as np

class Grafo:
    def __init__(self,tammatriz,es_dirigido = False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido
        self.matriz = np.zeros((tammatriz,tammatriz))

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
        return print(self.matriz)

    def vertices(self):
        return self.lista_vertices

    def insertar_conpeso(self, x, z, dis = 0,dirigido = False):
        if x == z:
            print(f"Mismo vertice no admitido:{x,z}")
            return
        """ Agregar el vértice de origen """
        if x not in self.lista_vertices:
            self.lista_vertices[x] = None
        """ Agregar el destino (ojo, x sumideros)"""
        if z not in self.lista_vertices:
            self.lista_vertices[z] = None

        nw = Vertice(z, dis,self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos += 1

    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print("->", end=' ')
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


    def de_matriz_a_lista(self,matriz, nombre = False):
        for origigen in range(len(matriz)):
            for destino in range(len(matriz)):
                if matriz[origigen][destino] == 1:
                    if nombre != False:
                        self.insertar(nombre[origigen],nombre[destino],True)
                    else:
                        self.insertar(origigen+1,destino+1,True)

    def armar_matriz_warshall(self,x ,y, dis):
        if x < 0 and x > len(self.matriz) and y <0 and y > len(self.matriz):
            print("fuera de rango")
        else:
            self.matriz[x-1][y-1] = dis


    def armar_matriz_desde_lista(self):
        """se armara una matriz de adyacencia, la cual tomara los vertices ordenados con sorted()
                la primer fila y columna sera el valor mas chico y la ultima fila y columna será el valor mas grande"""

        letras_unicas = []
        for key, valor in self.lista_vertices.items():
            arco = self.lista_vertices[key]
            if arco != None:
                lista = arco.devolverlistaadyacentes()
                for i in lista:
                    letras_unicas.append(i)
                letras_unicas.append(key)

        letras_unicas = sorted(set(letras_unicas))  #me quedo solo con la lsita de letras sin repetir

        # Crear la matriz de adyacencia
        tam = self.n_vertices()
        self.matriz = np.zeros((tam, tam))

        # Llenar matriz
        for origen, destinos in self.lista_vertices.items():
            arco = self.lista_vertices[origen]
            if arco != None:
                lista = arco.devolverlistaadyacentes()
                for destino in lista:
                    fila = letras_unicas.index(origen)
                    columna = letras_unicas.index(destino)
                    self.matriz[fila][columna] = arco.devovlerpeso(destino)


    def preparar_matriz(self):
        rangmat = len(self.matriz)
        for i in range(rangmat):
            for j in range(rangmat):
                if self.matriz[i][j] == 0:
                    self.matriz[i][j] = float('inf')

    def floyd_warshall(self):
        self.preparar_matriz()
        lista = sorted(self.lista_vertices)

        ranmat = len(self.matriz)
        for k in range(0, ranmat):
            for i in range(0, ranmat):
                for j in range(0, ranmat):
                    aux = self.matriz[i][j]
                    self.matriz[i][j] = min(self.matriz[i][j], self.matriz[i][k] + self.matriz[k][j])

                    if self.matriz[i][j] != float('inf') and self.matriz[i][j] != aux:  # no imprimo los que se quedaron iguales ni lso que se quedaron en inf
                        print(f'la distancia minima entre los vertices {lista[i]} {lista[j]} es ahora:{self.matriz[i][j]} antes era de {aux}  Se uso como conexion a {lista[k]}' )
                    """if self.matriz[i,j] > self.matriz[i,k] + self.matriz[k,j]:
                        self.matriz[i,j] = self.matriz[i,k] + self.matriz[k,j]"""


