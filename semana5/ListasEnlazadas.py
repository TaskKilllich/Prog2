class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.prim = None
        self.prox = None
        self.ulti = None
        self.ante = None

    def __str__(self):
        return self.dato

    def elelemento(self):
        return self.dato

    def __len__(self):
        return len(self)

    def anterior(self):
        return self.ante

    def enlazarProximo(self, otrodato):
        self.prox = otrodato

    def enlazarAnterior(self, otrodato):
        self.ante = otrodato


class ListaEnlazada:

    def __init__(self):
        self.prim = None
        self.ulti = None

    def len(self):
        contador = 0
        nodo_actual = self.prim
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.prox
        return contador

    def agregar_nodo(self, dato):
        #agrega un nodo a la listaEnlazada
        nuevo_nodo = Nodo(dato)
        if self.prim is None:
            #si no habia elementos agrega al principio
            self.prim = nuevo_nodo
            self.ulti = nuevo_nodo
        else:
            nodo_actual = self.prim
            while nodo_actual.prox is not None:
                nodo_actual = nodo_actual.prox
            nodo_actual.prox = nuevo_nodo
            self.ulti = nuevo_nodo

    def borrar_nodo(self, dato):
        if self.prim is None:
        #si no hay elementos en la lista no hace nada
            return 0

        if self.prim.dato == dato:
            #si el dato a borrar estaba al principio, le asigna el sigiente
            self.prim = self.prim.prox
            if self.prim is None:
                self.ulti = None
            return 0

        nodo_actual = self.prim
        while nodo_actual.prox is not None:
            #encuentra el dato y hace la conexion
            if nodo_actual.prox.dato == dato:
                nodo_actual.prox = nodo_actual.prox.prox
                if nodo_actual.prox is None:
                    self.ulti = nodo_actual
                return 0
            nodo_actual = nodo_actual.prox

    def borrar_por_posicion(self, pos):
        if self.prim is None:
            return False

        if self.len() < pos:
            return None

        if pos < 1:
            return None

        nodo_actual = self.prim

        if pos == 1:
            self.prim = nodo_actual.prox
            if self.prim is None:
                self.ulti = None
            return nodo_actual.dato

        for i in range(1, pos-1):
            nodo_actual = nodo_actual.prox          # cuando se llega a la 2 antes de la posicion original
            if nodo_actual.prox is None:     # Verificar que la posición sea válida
                return None

        if nodo_actual.prox.prox is None:    #si es el utlimo   ver como hacer para asignar el self.ulti bien
            print("aca")
            nodoborrado = nodo_actual.prox  # para mostrar que nodo fue borrado
            self.ulti = nodo_actual
            nodo_actual.prox = nodo_actual.prox.prox
            print("prim:", self.prim, "ulti:", self.ulti)
            return nodoborrado.dato

        nodoborrado = nodo_actual.prox  # para mostrar que nodo fue borrado
        nodo_actual.prox = nodo_actual.prox.prox        #hace las conexiones

        return nodoborrado.dato

    def imprimir_lista(self):
        valores = []
        nodo_actual = self.prim
        while nodo_actual is not None:
            valores.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.prox
        return "->".join(valores)

    def imprimirlistanumerada(self):
        if self.len() > 0:
            nodo_actual = self.prim
            print("----------------------")
            i = 1
            while nodo_actual is not None:
                print(f'{i}-{nodo_actual.dato}')
                i += 1
                nodo_actual = nodo_actual.prox
            print("----------------------")
            return
        print("Lista vacia")

    def imprimirLista(self):
        """Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos."""
        nodo_actual = self.prim
        print("[", end='')
        while nodo_actual is not None:
            if nodo_actual.prox == None:
                print(f"{nodo_actual.dato}]")
            else:
                print(nodo_actual.dato, end=',')
            nodo_actual = nodo_actual.prox

    def iguales(self, laotralista):
        #metodo que comparar dos listas ej3
        if self.len() != laotralista.len():
            return False
        nodo_actual_l1 = self.prim
        nodo_actual_l2 = laotralista.prim
        while nodo_actual_l1 != None:
            if nodo_actual_l1.dato != nodo_actual_l2.dato:
                return False
            nodo_actual_l1 = nodo_actual_l1.prox
            nodo_actual_l2 = nodo_actual_l2.prox
        return True

    def intercabiar(self, elemento, porposicion=False, pos=None):
        if self.prim is None:
            print("Imposible intercambiar, lista Vacia")
            return

        if self.prim == elemento and self.prim.prox is None:
            return

        if elemento == self.ulti:
            return

        if porposicion:
            elemento = self.obtener_elemento_segun_posicion(pos)
            if elemento is False:
                print("Error no existe la posicion:", pos)
                return

        try:
            elemento = int(elemento)    #por si el elemento era un int
        except ValueError:
            pass

        nodo_actual = self.prim
        while nodo_actual is not None:

            if nodo_actual.dato == elemento:

                if nodo_actual.prox is None:
                    return

                aux = nodo_actual.dato
                nodo_actual.dato = nodo_actual.prox.dato
                nodo_actual.prox.dato = aux
                return
            nodo_actual = nodo_actual.prox
        print("Elemento No encontrado")

    def obtener_elemento_segun_posicion(self, pos):
        if self.prim is None:
            return
        nodo_actual = self.prim
        index = 1
        while nodo_actual is not None:
            if index == pos:
                return nodo_actual.dato   #encontro el nodo
            nodo_actual = nodo_actual.prox
            index += 1
        return False

    def mesclarlistas(self, otralista, orden=False):
        nuevalista_l3 = ListaEnlazada()
        nodo_actual_l1 = self.prim
        nodo_actual_l2 = otralista.prim
        while nodo_actual_l1 is not None and nodo_actual_l2 is not None:
            nuevalista_l3.agregar_ordenado(nodo_actual_l1.dato, orden)
            nuevalista_l3.agregar_ordenado(nodo_actual_l2.dato, orden)
            nodo_actual_l1 = nodo_actual_l1.prox
            nodo_actual_l2 = nodo_actual_l2.prox

        while nodo_actual_l1 is not None:
            nuevalista_l3.agregar_ordenado(nodo_actual_l1.dato, orden)
            nodo_actual_l1 = nodo_actual_l1.prox

        while nodo_actual_l2 is not None:
            nuevalista_l3.agregar_ordenado(nodo_actual_l2.dato, orden)
            nodo_actual_l2 = nodo_actual_l2.prox
        return nuevalista_l3

    def agregar_ordenado(self, dato, mayoramenor=False):
        nuevo_nodo = Nodo(dato)
        if self.prim is None:
            self.prim = nuevo_nodo
            self.ulti = nuevo_nodo
            return
        if mayoramenor:
            actual_nodo = self.prim
            if nuevo_nodo.dato > actual_nodo.dato:
                nuevo_nodo.enlazarProximo(actual_nodo)
                self.prim = nuevo_nodo
            else:
                anterior_nodo = None
                while actual_nodo.dato >= nuevo_nodo.dato and actual_nodo.prox is not None:
                    anterior_nodo = actual_nodo
                    actual_nodo = actual_nodo.prox

                if actual_nodo.dato >= nuevo_nodo.dato:
                    nuevo_nodo.enlazarAnterior(actual_nodo)
                    actual_nodo.enlazarProximo(nuevo_nodo)
                    self.ulti = nuevo_nodo
                else:
                    nuevo_nodo.enlazarProximo(actual_nodo)
                    nuevo_nodo.enlazarAnterior(anterior_nodo)
                    anterior_nodo.enlazarProximo(nuevo_nodo)
                    actual_nodo.enlazarAnterior(nuevo_nodo)
        else:
            actual_nodo = self.prim
            if nuevo_nodo.dato < actual_nodo.dato:
                nuevo_nodo.enlazarProximo(actual_nodo)
                self.prim = nuevo_nodo
            else:
                anterior_nodo = None
                while actual_nodo.dato <= nuevo_nodo.dato and actual_nodo.prox is not None:
                    anterior_nodo = actual_nodo
                    actual_nodo = actual_nodo.prox

                if actual_nodo.dato <= nuevo_nodo.dato:
                    nuevo_nodo.enlazarAnterior(actual_nodo)
                    actual_nodo.enlazarProximo(nuevo_nodo)
                    self.ulti = nuevo_nodo
                else:
                    nuevo_nodo.enlazarProximo(actual_nodo)
                    nuevo_nodo.enlazarAnterior(anterior_nodo)
                    anterior_nodo.enlazarProximo(nuevo_nodo)
                    actual_nodo.enlazarAnterior(nuevo_nodo)
