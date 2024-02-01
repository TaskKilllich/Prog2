class Vertice:
    def __init__(self, dato=None,peso = 0, prox=None):
        self.dato = dato
        self.peso_arco = peso
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def valor(self):
        return self.dato

    def proximo(self):
        return self.prox

    def peso(self):
        return self.peso_arco
    def imprimirAlReves(self):
        if self.prox != None:
            self.prox.imprimirAlReves()
        print(self)

    def imprimeLista(nodo):
        """Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos."""
        while nodo:
            print(f'({nodo} :{nodo.peso()})', end=" ")
            nodo = nodo.prox
        print(" ")

    def devolverlistaadyacentes(nodo):
        lista = []
        while nodo:
            lista.append(nodo.dato)
            nodo = nodo.prox
        return lista

    def siguiente(self, unNodo):
        """ Engancha el nodo actual, self, con unNodo """
        self.prox = unNodo
