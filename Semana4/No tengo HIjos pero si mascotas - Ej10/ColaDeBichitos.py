"""Ejercicio 10
La veterinaria “No tengo hijos pero si mascotas” agrupa a un conjunto de 4 veterinarios donde se atienden
pequeños animales. De los tres veterinarios, uno se dedica a animales exóticos y los otros, a mascotas en general.
a) Escribir un TAD ColaDeBichitos, con los métodos nuevo_paciente, que recibe el nombre de la mascota y del
dueño y lo encola, y un método proximo_paciente que devuelva la siguiente mascota que debe ser atendida, y la
quite de la cola.
b) Escribir un TAD Recepción, que contenga un diccionario con las colas correspondientes a cada veterinario, y los
métodos nuevo_paciente que reciba el nombre de la mascota, de su dueño y del especialista, y proximo_paciente
que reciba el nombre del veterinario que terminó de atender y devuelva el próximo paciente que está esperando a
ese profesional.
c) Escribir un programa que permita al usuario ingresar nuevas mascotas o indicar que un veterinario se ha
liberado y en ese caso imprima el próximo paciente que lo está esperando"""

class ColaDeBichitos:
    def __init__(self):
        self.dato = []

    def nuevo_Bichito(self,mascota,duenio):
        self.dato.append((mascota,duenio))

    def proximo_Bichito(self):
        if not self.empty():
            return self.dato.pop()
        else:
            return True

    def empty(self):
        return (self.dato == [])

    def cantidad(self):
        return len(self.dato)
