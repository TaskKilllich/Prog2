from Vertices import *
import numpy as np
from Cola import *
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

    def insertar_en_matriz(self, x, z, dirigido=False):
        if x == z:
            print("Same vertex %d and %d" % x, z)
        self.matriz[x][z] = 1
        if dirigido:
            self.matriz[z][x] = 1

    def insertar(self, x, z, dirigido=False):
        if x == z:
            print(f"Mismo vertice no admitido:{x,z}")
            return
        """ Agregar el vértice de origen """
        if x not in self.lista_vertices:
            self.lista_vertices[x] = None
        """ Agregar el destino (ojo, x sumideros)"""
        if z not in self.lista_vertices:
            self.lista_vertices[z] = None

        nw = Vertice(z, self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos += 1

        if dirigido is False and z != x:
            self.insertar(z, x, True)

    def armar_matriz_desde_lista(self):
        """se armara una matriz de adyacencia, la cual tomara los vertices ordenados con sorted()
        la primer fila y columna sera el valor mas chico y la ultima fila y columna será el valor mas grande"""
        letras_unicas = []
        for key, valor in self.lista_vertices.items():
            arco = self.lista_vertices[key]
            if arco is not None:
                lista = arco.devolverlistaadyacentes()
                for i in lista:
                    letras_unicas.append(i)
                letras_unicas.append(key)
        # me quedo solo con la lsita de letras sin repetir
        letras_unicas = sorted(set(letras_unicas))
        # Crear la matriz llena de 0ros segun la cantida de vertices
        tam = self.n_vertices()
        self.matriz = np.zeros((tam, tam))
        # Llenar matriz
        for origen, destinos in self.lista_vertices.items():
            arco = self.lista_vertices[origen]
            if arco is not None:
                lista = arco.devolverlistaadyacentes()
                for destino in lista:
                    fila = letras_unicas.index(origen)
                    # con index obtengo la posicion en la que tendria que ir un 1
                    columna = letras_unicas.index(destino)
                    self.matriz[fila][columna] = 1

    def imprimir(self):
        verticesordenados = sorted(self.lista_vertices)
        for vertice in verticesordenados:
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
            return self.lista_vertices[x]

    def bfs(self, vert):
        estado = {}
        padre = {}
        vertices = self.vertices()
        q = Cola()
        for ve in vertices:
            if ve != vert:
                estado[ve] = "N"
                padre[ve] = None
        estado[vert] = "D"
        padre[vert] = None
        q.encolar(vert)
        while not q.empty():
            u = q.desencolar()
            print(u)  # Procesar!!
            adyacente = vertices[u]
            while adyacente:
                valor = adyacente.valor()
                # Procesar arista
                if estado[valor] == "N":
                    estado[valor] = "D"
                    padre[valor] = u
                    q.encolar(valor)
                adyacente = adyacente.proximo()
            estado[u] = "P"

    def encontrar_sumideros_lista(self):
        sumideros = []
        for ver in range(self.n_vertices()):
            adyacentes = self.lista_vertices[ver]
            if len(adyacentes) == 0:
                sumideros.append(ver)
        return sumideros

    def encontrar_sumideros_matriz(self):
        sumideros = []
        for ver in range(self.n_vertices()):
            fila = self.matriz[ver]
            if sum(fila) == 0:
                sumideros.append(ver)
        return sumideros

    def de_matriz_a_lista(self, matriz, nombre=False):
        for origigen in range(len(matriz)):
            for destino in range(len(matriz)):
                if matriz[origigen, destino] == 1:
                    if nombre is not False:
                        self.insertar(nombre[origigen], nombre[destino], True)
                    else:
                        self.insertar(origigen+1, destino+1, True)

    def gradosIOmatriz(self,vertice):
        gradoio = {'entrada:':None,
                    'salida:':None}
        counto = 0
        counti = 0
        if vertice in self.lista_vertices:
            list = sorted(self.lista_vertices)
            pos = list.index(vertice)

            for i in range(self.n_vertices()):
                if self.matriz[pos][i] == 1:
                    counto += 1
                if self.matriz[i][pos] == 1:
                    counti += 1
            gradoio['entrada:'] = counti
            gradoio['salida:'] = counto
            return gradoio
        return False

    def gradoIOLista(self, vertice):
        gradoio = {'entrada:': None,
                   'salida:': None}
        counto = 0
        counti = 0
        if vertice in self.lista_vertices:
            for nodo_origen in self.lista_vertices:
                if self.lista_vertices[nodo_origen] is not None:
                    if vertice in self.lista_vertices[nodo_origen].devolverlistaadyacentes():
                        counti += 1
            if self.lista_vertices[vertice] is not None:
                counto = len(self.lista_vertices[vertice].devolverlistaadyacentes())
            gradoio['entrada:'] = counti
            gradoio['salida:'] = counto
            return gradoio
        return False
    def gradoIOMatriz_todos(self):
        gradoio = {}
        counto = 0
        counti = 0
        for i in range(self.n_vertices()):
            for j in range(self.n_vertices()):
                if self.matriz[j][i] == 1:
                    counti += 1
                if self.matriz[i][j] == 1:
                    counto += 1
            gradoio[i+1] = counti, counto
            counto = 0
            counti = 0
        return gradoio

    def gradoIOLista_todos(self):
        grado_io = {}
        for key in self.lista_vertices:
            arco = self.lista_vertices[key]
            grado_i = 0

            for nodo_origen in self.lista_vertices:
                if self.lista_vertices[nodo_origen] is not None:
                    if key in self.lista_vertices[nodo_origen].devolverlistaadyacentes():
                        grado_i += 1
            if arco is not None:
                grado_o = len(arco.devolverlistaadyacentes())
            else:
                grado_o = 0
            grado_io[key] = grado_i, grado_o
        return grado_io

    def sumideros(self):
        sumidero = {'sumidero:': [],
                    'fuentes:': []}
        for key in self.lista_vertices:
            arco = self.lista_vertices[key]
            fuentes = True
            sumisalida = True
            # para ir iterando y no usar un for
            listavert = list(self.lista_vertices.keys())

            while listavert and fuentes:
                nodo_actual = listavert.pop(0)

                if self.lista_vertices[nodo_actual] is not None:
                    if key in self.lista_vertices[nodo_actual].devolverlistaadyacentes():
                        fuentes = False
            if arco is not None:
                sumisalida = False

            if fuentes is True:
                sumidero['fuentes:'].append(key)
            if sumisalida is True:
                sumidero['sumidero:'].append(key)
        return sumidero
