class Pila:

    def __init__(self):
        self.elementos = []


    def push(self,unacosa):
        self.elementos.append(unacosa)          #agrega un elemento a la pila, en la ultima poscioion

    def pop(self):
        if len(self.elementos) == 0:
            return print("NO SE PUEDE DESAPILAR PORQUE LA PILA YA ESTA VACIA.")
        else:
            return self.elementos.pop()     #saca el ultimo elemento de la pila

    def empty(self):
        return (self.elementos == [])       #se fija si la lista de elementos esta vacia o no

    def espejar(self):
        aux = []
        while not self.empty():
            aux.append(self.pop())
        for i in aux:
            self.push(i)
