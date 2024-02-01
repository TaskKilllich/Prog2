
class Cola:
        def __init__(self,sigiente = None):

            self.elementos = []

        def __len__(self):
            return len(self.elementos)


        def encolar(self, unacosa):
            self.elementos.append(unacosa)

        def desencolar(self):
            return self.elementos.pop(0)

        def empty(self):
            return (self.elementos == [])

        def espejar(self):
            aux = []
            while not self.empty():
                aux.append(self.desencolar())
            for i in aux[::-1]:
                self.encolar(i)

