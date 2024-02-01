class Pila:

    def __init__(self):
        self.dato = []


    def apilar(self,unacosa):
        self.dato.append(unacosa)          #agrega un elemento a la pila, en la ultima poscioion

    def desapilar(self):
        if len(self.dato) == 0:
            return
        else:
            return self.dato.pop()     #saca el ultimo elemento de la pila

    def esta_vacia(self):
        return (self.dato == [])       #se fija si la lista de elementos esta vacia o no

    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.dato[-1]