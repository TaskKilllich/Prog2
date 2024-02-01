"""Nº de Alumno, DNI, Apellido, Nombre, Código de carrera que cursa, y los finales que tiene rendidos (código de
materia, fecha, nota)."""
class Alumno:
    def __init__(self,alu_id,alu_dni,alu_apell,alu_nom,alu_c_cur,alu_finales):
        self.alu_id = alu_id
        self.alu_dni = alu_dni
        self.alu_apell = alu_apell
        self.alu_nom = alu_nom
        self.alu_c_cur = alu_c_cur
        self.alu_finales = [alu_finales]
        self.prox = None
        self.ante = None

    def __str__(self):
        return "{} {}, {} , {}".format(self.alu_id, self.alu_apell, self.alu_nom, self.alu_dni)

    def numero_alumno(self):
        return self.alu_id

    def enlazarProximo(self, otroAlu):
        self.prox = otroAlu

    def enlazarAnterior(self, otroAlu):
        self.ante = otroAlu

    def finales(self):
        return self.alu_finales

    def agregar_final(self,datosfinal):
        self.alu_finales.append(datosfinal)

    def proximo(self):
        return self.prox

    def anterior(self):
        return self.ante

    def imprimir(self):
        print("{} {} {} {} {}".format(self.alu_id, self.alu_dni, self.alu_apell, self.alu_nom, self.alu_c_cur))

        if self.finales() == [None]:
            print("Sin finales")
            print("---")
            return

        for exfi in self.alu_finales:
            if exfi != None:
                print("     {} ".format(exfi))
        print("---")



class ListaAlumnos:
    def __init__(self):
        self.prim = None
        self.ulti = None
        self.materiasycodigo = {"IF003": "Algorítmica y Programación I",
                         "IF006": "Algorítmica y Programación II",
                         "IF010": "Analisis y Diseño de Sistemas",
                         "IF002": "Expresión de Problemas y Algoritmos",
                         "IF001": "Elementos de Informática",
                         "MA045": "Algebra",
                         "MA008": "Matematica Discreta",
                         "MA006": "Estadistica",
                         "FA007": "Ingles",
                         "MA046": "Analisis Matematico",
                         "IF004": "Sistema y Organizaciones",
                         "IF005": "Arquitectura de computadoras"}

    def len(self):
        contador = 0
        nodo_actual = self.prim
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.prox
        return contador

    def primero(self):
        return self.prim

    def agregar_alu(self,alu_id,alu_dni,alu_apell,alu_nom,alu_c_cur,alu_finales=None):
        nuevo_alu = Alumno(alu_id,alu_dni,alu_apell,alu_nom,alu_c_cur,alu_finales)
        if self.len() == 0:
            self.prim = nuevo_alu
            self.ulti = nuevo_alu
            return
        actual_alu = self.prim

        if nuevo_alu.numero_alumno() < actual_alu.numero_alumno():
            #al principio
            nuevo_alu.enlazarProximo(actual_alu)
            self.prim = nuevo_alu
        else:
            anterior_alu = None
            while actual_alu.numero_alumno() <= nuevo_alu.numero_alumno() and actual_alu.prox is not None:
                anterior_alu = actual_alu
                actual_alu = actual_alu.prox
            if actual_alu.numero_alumno() <= nuevo_alu.numero_alumno():
                nuevo_alu.enlazarAnterior(actual_alu)
                actual_alu.enlazarProximo(nuevo_alu)
                self.ulti = nuevo_alu
            else:
                nuevo_alu.enlazarProximo(actual_alu)
                nuevo_alu.enlazarAnterior(anterior_alu)
                anterior_alu.enlazarProximo(nuevo_alu)
                actual_alu.enlazarAnterior(nuevo_alu)



    def remove(self, alu_id):
        # quita de la lista y devuelve el alumno con un cierto id
        if self.len() == 0:
            print("No hay elementos en la lista")
            return
        actual_alu = self.prim
        anterior_alu = None
        i=0
        while actual_alu.numero_alumno() != alu_id and actual_alu.proximo() is not None:
            anterior_alu = actual_alu
            actual_alu = actual_alu.prox

        if actual_alu.numero_alumno() != alu_id:
            print("El Alumno {} no existe".format(alu_id))
            return

        if anterior_alu == None:
            ## Borrar el primer alumno de la lista
            self.prim = actual_alu.prox
            if self.prim != None:
                self.prim.enlazarAnterior(actual_alu.ante)
            else:
                ## Era el primer y único alumno de la lista!!
                self.ulti = None
        elif actual_alu.prox is None:
            ## Es el último alumno de la lista
            anterior_alu.enlazarProximo(actual_alu.prox)
            self.ulti = anterior_alu
        else:
            ## Es un alumno del medio
            anterior_alu.enlazarProximo(actual_alu.prox)
            actual_alu.prox.enlazarAnterior(actual_alu)

        return actual_alu

    def imprimir_alumnos(self):
        if self.len() == 0:
            return False
        actual_alu = self.prim
        while actual_alu is not None:
            print(actual_alu)
            actual_alu = actual_alu.prox

    def imprimir_materias(self):
        print("------------------------------------------------")
        for clave, valor in self.materiasycodigo.items():
            print(clave,'-',valor)
        print("------------------------------------------------")

    def verifica_code_materia(self,codigo_mat):
        if codigo_mat not in self.materiasycodigo:
            return False

    def imprimir_datos(self):
        if self.len() == 0:
            return False
        actual_alu = self.prim
        while actual_alu is not None:
            actual_alu.imprimir()
            actual_alu = actual_alu.prox

    def validar_id(self,id):
        if self.len() == 0:
            return
        actual_alu = self.prim
        while actual_alu is not None:
            if actual_alu.numero_alumno() == id:
                #si el ya hay un alumno cargado con el mismo id devuelve un true y el nombre de dicho alumno
                return True, actual_alu
            actual_alu = actual_alu.prox
        return id, None

    def imprimir_segun_id(self, id):
        if self.len() == 0:
            return
        actual_alu = self.prim
        while actual_alu is not None:
            if actual_alu.numero_alumno() == id:
                return actual_alu
            actual_alu = actual_alu.prox
        return False

    def agregar_finales(self,id,finaldado):
        actual_alu = self.prim
        while actual_alu is not None:
            if actual_alu.numero_alumno() == id:
                actual_alu.agregar_final(finaldado)
                return
            actual_alu = actual_alu.prox
