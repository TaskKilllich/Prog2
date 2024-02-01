class ArbolB:
    def __init__(self,dato,izq=None,der=None):
        self.dato = dato
        self.der = der
        self.izq = izq

    def __str__(self):
        return str(self.dato)

    def printInfijo(self):
        if self.izq is not None:
            return

    def insertar(self, valor):

            #pone el valor en el lado izquierdo si el siguiente es un None, sino llama devuelta al metodo
        if self.der is None:
            self.der = ArbolB(valor)

        elif self.izq is None:
            self.der.insertar(valor)

        else:
            if self.izq is None:
                self.izq = ArbolB(valor)
            else:
                self.izq.insertar(valor)

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


def sizeA(arbol):
    if arbol == None:
        return 0
    return 1+sizeA(arbol.izq) + sizeA(arbol.der)

def alturaA(arbol):
    if arbol == None:
        return -1
    alt_izq = alturaA(arbol.izq)
    alt_der = alturaA(arbol.der)
    return 1+max(alt_izq,alt_der)
