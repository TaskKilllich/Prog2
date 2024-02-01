from Vertices import *
import numpy as np
from Cola import *
class Grafo:
    def __init__(self, cantidad_vert, es_dirigido=False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido
        self.matriz = np.zeros((cantidad_vert, cantidad_vert))

    def __str__(self):
        return "G = ("+str(self.n_vertices())+" V, "+str(self.n_arcos)+" A)"

    def n_vertices(self):
        return len(self.matriz)

    def dirigido(self):
        return self.es_dirigido

    def n_arcos(self):
        return self.n_arcos

    def ver_matriz(self):
        for i in range(self.n_vertices()):
            print(f'  {i + 1}', end='')
        print()
        print(self.matriz)
        return

    def vertices(self):
        return self.lista_vertices

    def insertar_en_matriz(self, x, z, dirigido=False):

        if x > self.n_vertices()-1 or z > self.n_vertices()-1 or x < 0 or z < 0:
            print("Posicion fuera de rango")
            return
        elif x == z:
            print(f"Mismo vertice no admitido:{x,z}")
        else:
            self.matriz[x][z] = 1
        if dirigido is False:
            self.matriz[z][x] = 1

    def insertar(self, x, z, dirigido=False):

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
        print(letras_unicas)
        # Crear la matriz llena de 0ros segun la cantida de vertices
        tam = self.n_vertices()
        self.matriz = np.zeros((tam, tam))
        print(self.matriz)
        # Llenar matriz
        for origen, destinos in self.lista_vertices.items():
            arco = self.lista_vertices[origen]
            if arco is not None:
                lista = arco.devolverlistaadyacentes()
                for destino in lista:
                    # con index obtengo la posicion en la que tendria que ir un 1
                    fila = letras_unicas.index(origen)
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

    def de_matriz_a_lista(self, matriz, nombre=False):
        #recive una matriz creada por el usuario e inserta los elementos para crear la lista
        for origigen in range(self.n_vertices()):
            for destino in range(self.n_vertices()):
                if matriz[origigen, destino] == 1:
                    if nombre is not False:
                        self.insertar(nombre[origigen], nombre[destino], True)
                    else:
                        self.insertar(origigen+1, destino+1, True)



    """def bfs(self, vert):
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
            estado[u] = "P"""

    def obtener_adyacentes(self, vertice):
        adyacentes = []
        for i in range(self.n_vertices()):
            if self.matriz[vertice][i] == 1:
                adyacentes.append(i)
        return adyacentes

    def bfs(self, vert):
        if vert < 0 or vert >= self.n_vertices():
            print("El vértice está fuera de rango.")
            return 0
        # lleno un vector de Falses segun a cantidad de vertices
        visitados = [False] * self.n_vertices()

        q = Cola()

        visitados[vert] = True
        q.encolar(vert)

        while not q.empty():
            vertice_actual = q.desencolar()

            if len(q) != 0 or vertice_actual == vert:
                print(f"{vertice_actual+1} ->", end=" ")
            else:
                print(f"{vertice_actual+ 1} ", end=" ")

            adyacentes = self.obtener_adyacentes(vertice_actual)
            for adyacente in adyacentes:
                if not visitados[adyacente]:
                    visitados[adyacente] = True
                    q.encolar(adyacente)

    def gradoIOMatriz(self):
        gradoIO = {}
        countO = 0
        countI = 0
        for i in range(self.n_vertices()):
            for j in range(self.n_vertices()):
                if self.matriz[j][i] == 1:
                    countI += 1
                if self.matriz[i][j] == 1:
                    countO += 1
            gradoIO[i+1] = countI, countO
            countO = 0
            countI = 0
        return gradoIO

    def gradoIOLista(self):
        gradoIO = {}
        for key in self.lista_vertices:
            arco = self.lista_vertices[key]
            gradoI = 0
            for nodo_origen in self.lista_vertices:
                if key in self.lista_vertices[nodo_origen].devolverlistaadyacentes():
                    gradoI += 1
            if arco is not None:
                gradoO = len(arco.devolverlistaadyacentes())
            else:
                gradoO = 0
            gradoIO[key] = gradoI, gradoO
        return gradoIO
