class Vertice:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def valor(self):
        return self.dato

    def proximo(self):
        return self.prox

    def imprimirAlReves(self):
        if self.prox != None:
            self.prox.imprimirAlReves()
        print(self)

    def imprimeLista(nodo):
        """Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos."""
        while nodo:
            print(nodo, end=" ")
            nodo = nodo.prox
        print(" ")

    def devolverlistaadyacentes(nodo):
        lista = []
        while nodo is not None:
            lista.append(nodo.dato)
            nodo = nodo.prox
        return lista

    def siguiente(self, unNodo):
        """ Engancha el nodo actual, self, con unNodo """
        self.prox = unNodo
