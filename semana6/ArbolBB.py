#binario de busqueda
class ArbolBB:
    def __init__(self, dato=None, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der
        self.raiz = None

    def __str__(self):
        return str(self.dato)

    def valor(self):
        return self.dato

    def subder(self):
        return self.der

    def subizq(self):
        return self.izq

    def insertar(self, valor):
        if self.dato is None:
            self.dato = valor
            self.raiz = valor

        elif valor < self.dato:
            #pone el valor en el lado izquierdo si el siguiente es un None, sino llama devuelta al metodo
            if self.izq is None:
                self.izq = ArbolBB(valor)
            else:
                self.izq.insertar(valor)
        elif valor > self.dato:
            if self.der is None:
                self.der = ArbolBB(valor)
            else:
                self.der.insertar(valor)
        else:
            print("El Dato ya existe")

    def insertar_no_bus(self, x):
        #inserta los datos de izquierda a derecha, sin comparar los valores
        if self.izq is None:
            self.izq = ArbolBB(x)
        elif self.der is None:
            self.der = ArbolBB(x)
        elif self.izq.izq is None or self.izq.der is None:
            self.izq.insertar_no_bus(x)
        else:
            self.der.insertar_no_bus(x)

    def insertar_no_bus2(self, valor):
        #inserta los elementos en un arbol solo fijandose que quede balanceado, anda mal
        if self.dato is None:
            self.dato = valor

        if self.izq is None:
            self.izq = ArbolBB(valor)

        elif self.der is None:
            self.der = ArbolBB(valor)

        else:
            altura_izq = alturaB(self.izq)
            altura_der = alturaB(self.der)
            if altura_izq <= altura_der:
                self.izq.insertar_no_bus2(valor)
            else:
                self.der.insertar_no_bus2(valor)

    def imprimir(self):
        """ Recorre e imprime en orden los nodos de un ABB """
    # Si el subárbol está vacío, al aplicar el método da un error,
    # porque imprimir no está definido para el tipo None.
    # Por eso se pregunta (valida) que no sea None.
        if self.izq is not None:
            self.izq.imprimir()
        print(self.dato, end=" ")
        if self.der is not None:
            self.der.imprimir()

    def imprimirlevel(self):
        levels = [self]
        while levels:
            print(' '.join(str(node) for node in levels))
            next_level = list()
            for i in levels:
                if i.izq:
                    next_level.append(i.izq)
                if i.der:
                    next_level.append(i.der)
                levels = next_level

    def buscar(self, valor):
        if self.dato == valor:
            return valor
        elif self.dato > valor:
            if self.izq is not None:
                return self.izq.buscar(valor)
        elif self.dato < valor:
            if self.der is not None:
                return self.der.buscar(valor)
        return None

    def minimo(self):
        #va hasta el hijo de mas a la izq
        if self.dato is not None:
            minn = self
            while minn.izq is not None:
                minn = minn.izq
            return minn.dato

    def maximo(self):
        # va hasta el hijo de mas a la der
        if self.dato is not None:
            maxn = self
            while maxn.der is not None:
                maxn = maxn.der
            return maxn.dato

    def borrar_nodo(self, valor):

        if self is None:
            return False
        if self.raiz == valor:
            return False

        if valor < self.dato:
            if self.izq:
                self.izq = self.izq.borrar_nodo(valor)
            else:
                return False

        elif valor > self.dato:
            if self.der:
                self.der = self.der.borrar_nodo(valor)
            else:
                return False
        else:
            # no tiene hijos
            if self.izq is None and self.der is None:
                return None
                #solo hijo izq
            elif self.izq is not None and self.der is None:
                return self.izq
            #solo hijo der
            elif self.izq is None and self.der is not None:
                return self.der
            #tiene dos hijos
            else:
                sucesor = self.der.minimo()
                self.dato = sucesor.dato
                self.der = self.der.borrar_nodo(sucesor.dato)

        return self


def alturaA(arbol):
    if arbol is None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)
    return 1+max(alt_izq, alt_der)


def alturaB(arbol):
    if arbol is None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)
    return alt_izq, alt_der


def contarhojas(arbol):
    if arbol is None:
        return 0
    if arbol.subizq() is None and arbol.subder() is None:
        return 1
    return contarhojas(arbol.subder()) + contarhojas(arbol.subizq())


def es_busqueda_recursivo(nodo):
    if nodo is None:
        return True

    if nodo.subizq() and nodo.subizq().valor() > nodo.valor():
        return False

    if nodo.subder() and nodo.subder().valor() < nodo.valor():
        return False

    return es_busqueda_recursivo(nodo.subizq()) and es_busqueda_recursivo(nodo.subder())


def imprimirRango(nodo, valor_bajo, valor_alto):
    # recorrido hasta el mayor y menor guardando por donde pasa
    if not nodo.raiz:
        return False
    recorrido = []
    hastaelmenor(nodo, valor_bajo, recorrido)
    hastaelmayor(nodo, valor_alto, recorrido)
    return recorrido


def hastaelmenor(nodo, valor_bajo,recorrido):
    if valor_bajo == nodo.dato:
        recorrido.append(nodo.dato)
        return

    recorrido.append(nodo.dato)

    if valor_bajo < nodo.dato:
        hastaelmenor(nodo.izq,valor_bajo,recorrido)

    if valor_bajo > nodo.dato:
        hastaelmayor(nodo.der, valor_bajo, recorrido)


def hastaelmayor(nodo, valor_alto, recorrido):
    if valor_alto == nodo.dato:
        recorrido.append(nodo.dato)
        return
    if not nodo.raiz:
        recorrido.append(nodo.dato)

    if valor_alto < nodo.dato:
        hastaelmenor(nodo.izq, valor_alto, recorrido)

    if valor_alto > nodo.dato:
        hastaelmayor(nodo.der, valor_alto, recorrido)


def arbol_genealogico(nodo):
    nombre = input(f"Ingrese el nombre de la Madre de {nodo.dato} :")
    if nombre.lower() != 'no se' and nombre.lower() != 'no sé' and nombre != '':
        nombre = nombre.capitalize()
        nodo.insertar_no_bus(nombre)

    nombre = input(f"Ingrese el nombre de la Padre de {nodo.dato} :")

    if nombre.lower() != 'no se' and nombre.lower() != 'no sé' and nombre != '':
        nombre = nombre.capitalize()
        nodo.insertar_no_bus(nombre)
    if nodo.subizq() is not None:
        arbol_genealogico(nodo.subizq())
    if nodo.subder() is not None:
        arbol_genealogico(nodo.subder())





