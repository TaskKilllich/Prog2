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

from ColaDeBichitos import *

class Recepcion:
    def __init__(self):
        self.Veterinario = {'Richard Assmann': (ColaDeBichitos(),'General'),
                            'Erich Hintzsche': (ColaDeBichitos(),'General'),
                            'Magnus Hirschfeld': (ColaDeBichitos(),'General'),
                            'Carl Sachs': (ColaDeBichitos(),'Exotica')}

    def nuevo_paciente(self, doctor, mascota, dueno, ):
        if doctor in self.Veterinario:
            self.Veterinario[doctor][0].nuevo_Bichito(mascota, dueno)
        else:
            print("Especialista no encontrado.")

    def proximo_paciente(self, doctor):
        if doctor in self.Veterinario:
            return self.Veterinario[doctor][0].proximo_Bichito()


    def cantidad(self,doctor):
        return self.Veterinario[doctor][0].cantidad()

    def devolvernombrevet(self,numero):
        list_veterinarios = list(self.Veterinario.keys())
        try:
            veterinario = list_veterinarios[numero - 1]
        except IndexError:
            return False
        else:
            return veterinario

    def Lista_Veterinario(self):
        cont = 1
        for nombre, (cola, especialidad) in self.Veterinario.items():
            if self.cantidad(nombre) != 0:
                print("{0:2d}-{1:20s} | Especialidad: {2:10s} | En espera: {3:2d} ".format(cont,nombre, especialidad,self.cantidad(nombre)))
            else:
                print("{0:2d}-{1:20s} | Especialidad: {2:10s} | En espera: Libre ".format(cont,nombre, especialidad))
            cont+=1