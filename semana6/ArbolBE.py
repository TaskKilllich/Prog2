from Pila import *

class ArbolBE:
    def __init__(self,dato=None):
        self.dato = dato
        self.der = None
        self.izq = None
        self.operadores = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.resultad = ''
        self.polish = []
        self.pila = Pila()
        self.pilasubarboles = Pila()

    def __str__(self):
        return str(self.dato)

    def valor(self):
        return self.dato

    def subder(self):
        return self.der

    def subizq(self):
        return self.izq

    def resultado(self):
        print(self.pila.dato)

    def evaluar(self,expresion):
        duplicado = ['++','- -','**','//','+-','-+','*+','/+','+*','+/','-*','-/','*-','*/','/-','/*']
        check = ''.join(expresion)
        for i in duplicado:
            if i in check:
                print("asd")
                return False,None   #primero evaluo si no hay signos repetidos o mal ingresados
        else:
            self.make_RPN(expresion)
            rpm = self.polish.copy()
            print(self.polish)
            validacion = self.PolacaCheck(rpm)

            return validacion, self.polish
            #retono si la validacion es verdera o falsa y la polaca que se creo
            #tambien se podria armar el arbol desde aca directamente
    def PolacaCheck(self, rpn):
        #valida utilizando el metodo de polaca inversa
        if len(rpn) == 0:
            return True

        elemento = rpn.pop(0)

        if elemento.isdigit() or elemento[0] == '-':
            self.pila.apilar(elemento)

        else:
            n1 = self.pila.desapilar()
            n2 = self.pila.desapilar()
            try:
                res = str(eval(n1+elemento+n2))

                self.pila.apilar(res)
            except SyntaxError:
                return False
            #podria ir armado el resultado para luego devolverlo desde aca pero no llegue
        return self.PolacaCheck(rpn)

    def make_RPN(self, expresion):
        #crea de string a polaca inversa
        if len(expresion) == 0:
            while not self.pila.esta_vacia():
                self.polish.append(self.pila.desapilar())

            return True

        else:
            elemento = expresion.pop(0)
            if elemento == '-' and expresion[0].isdigit():
                elemento += expresion.pop(0)
                self.polish.append(elemento)

            if elemento.isdigit():
                self.polish.append(elemento)

            elif elemento in self.operadores:

                while not self.pila.esta_vacia() and self.pila.ver_tope() in self.operadores and self.operadores[elemento] <= self.operadores[self.pila.ver_tope()]:
                    self.polish.append(self.pila.desapilar())

                self.pila.apilar(elemento)

            elif elemento == '(':
                self.pila.apilar(elemento)

            elif elemento == ')':
                while not self.pila.esta_vacia() and self.pila.ver_tope() != '(':
                    self.polish.append(self.pila.desapilar())
                if not self.pila.esta_vacia() and self.pila.ver_tope() == '(':
                    self.pila.desapilar()

            return self.make_RPN(expresion)



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
    alt_izq = alturaA(arbol.subizq())
    alt_der = alturaA(arbol.subder())
    return 1+max(alt_izq,alt_der)

def construir_arbole(expresion):
    if not expresion:
        return None

    elemento = expresion.pop()
    nodo = ArbolBE(elemento)

    if elemento.isdigit() or (elemento.startswith('-') and elemento[1:].isdigit()):
        return nodo

    nodo.izq = construir_arbole(expresion)
    nodo.der = construir_arbole(expresion)

    return nodo


"""(-2*8)/(-5-3)"""