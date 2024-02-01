def FunImprimirAlReves(listaN):
    """ Es igual a imprimeLista(nodo) no es método, sino función"""
    if listaN == None:
        return
    cabeza = listaN
    cola = listaN.prox
    FunImprimirAlReves(cola)
    print(cabeza.dato)
    
class Nodo:
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
        while nodo:
            lista.append(nodo.dato)
            nodo = nodo.prox
        return lista

    def siguiente(self, unNodo):
        """ Engancha el nodo actual, self, con unNodo """
        self.prox = unNodo


class ListaE:
    """Modela una lista enlazada."""

    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)     
        self.prim = None

    def __str__(self):
        """ Presenta la lista como las listas de Python """
        tx = "["
        if self.empty():
            tx += "]"
        else:
            n = self.prim
            while (n != None):
                tx += str(n)+", "
                n = n.proximo()
            tx = tx[:-2]+"]"
        return tx
    
    def __len__(self):
        """ Devuelve la longitud de la lista""" 
        n = self.prim
        long = 0
        while (n != None):
            long += 1
            n = n.proximo()
        return long  

    def append(self, dato):
        """ agrega un dato al final de la lista """
        nuevoNodo = Nodo(dato)
        if self.prim == None:
            self.prim = nuevoNodo
        else:
            n = self.prim
            while (n.prox != None):
                n = n.prox
            n.prox = nuevoNodo
    
    def insert(self, i, x):
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""

        if i < 0:
             raise IndexError("Posición inválida")

        nuevo = Nodo(x)

        if i == 0:
            # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            n_act = self.prim
            pos = 0
            while (pos < i and n_act != None):
                n_ant = n_act
                n_act = n_act.prox
                pos += 1
            if (pos > i or n_act == None):
                raise IndexError("Posición inválida")
            
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

    def empty(self):
        """ Devuelve True/False """
        return (self.prim == None)
    
    def remove(self, x):
        
        """Elimina el elemento x """
        """Si x no existe o self es vacía, levanta ValueError"""

        if self.empty():
            raise ValueError("listaE.eliminar(x): x no está en la lista")

        act = self.prim
        if act.valor() == x:
            # Caso particular: eliminar el primero
            self.prim = act.proximo()
        else:
            # Buscar el nodo anterior a la posición deseada
            while (act.proximo() != None and act.proximo().valor() != x):
                act = act.proximo()

            if act.proximo() == None:
                # El valor no existe en la lista
                raise ValueError("listaE.eliminar(x): x no está en la lista")
            
            """ Enganchar el nodo actual con el próximo"""
            act.siguiente(act.proximo().proximo())

            
    def imprimirAlReves(self):
        if self.prim == None:
            return
        self.prim.imprimirAlReves()
     

class Grafo:
    def __init__(self, es_dirigido = False):
        self.lista_vertices = {}
        self.n_arcos = 0
        self.es_dirigido = es_dirigido

    def __str__(self):
        return "G = ("+str(self.n_vertices())+" V, "+str(self.n_arcos)+" A)"

    def n_vertices(self):
        return len(self.lista_vertices)

    def dirigido(self):
        return self.es_dirigido

    def vertices(self):
        return self.lista_vertices

    def n_arcos(self):
        return self.n_arcos

    def insertar(self, x, z, dirigido = False):
        """ Agregar el vértice de origen """
        if x not in self.lista_vertices:
            self.lista_vertices[x]= None
        """ Agregar el destino (ojo, x sumideros)"""
        if z not in self.lista_vertices:
            self.lista_vertices[z]= None

        nw = Nodo(z, self.lista_vertices[x])
        self.lista_vertices[x] = nw
        self.n_arcos+=1
        if dirigido is False and z != x:
            self.insertar(z,x, True)

    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')
            arco = self.lista_vertices[vertice]
            if arco is not None:
                print("->", end=' ')
                arco.imprimeLista()
            else:
                print("")
