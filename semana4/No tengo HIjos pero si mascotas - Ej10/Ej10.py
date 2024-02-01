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
import random

from Recepcion import *


def ingresarmascota():

    veteri = 1
    while veteri != 0:
        print("--Veterinarios activos--")
        re.Lista_Veterinario()
        print("**Ingrese un 0 para volver")
        try:
            veteri = int(input("seleccione a un veterinario:"))
        except ValueError:
            print("--ERROR:seleccione usando los numeros, intente nuevamente\n")
        else:
            if veteri != 0:
                Nom_duenio = input("Su Nombre:")
                Nom_Mascota = input("Nombre de su mascota:")
                if Nom_duenio != '' and Nom_Mascota != '':
                    Nom_Veteri = re.devolvernombrevet(veteri)
                    if Nom_Veteri != False:
                        re.nuevo_paciente(Nom_Veteri,Nom_Mascota,Nom_duenio)
                        print("\n _______________________________________________________________________________________")
                        print("| su mascota:{} ahora esta en la lista de espera para el Veterinario:{} |".format(Nom_Mascota,Nom_Veteri))
                        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
                    else:
                        print("\n--Error: Opcion no valida, intente nuevamente\n")
                else:
                    print("Datos no validos, intente nuevamente\n")
            else:
                print("terminando carga...\n")
    return 0


def liberarmascota():
    print("--Veterinarios activos--")
    re.Lista_Veterinario()
    try:
        vet = int(input("Seleccione a un veterinario:"))
    except ValueError:
        print("seleccione usando los numeros, intente nuevamente")
    else:
        vet = re.devolvernombrevet(vet)
        if vet != False:
            proximo = re.proximo_paciente(vet)

            if proximo != True:
                if random.randrange(1,99) != 13:
                    print("la mascota de {} {} volvio feliz a su casa :D".format(proximo[0], proximo[1]))
                else:
                    print("lamentablemente la operacion salio mal para {} la mascota de {} :(".format(proximo[0], proximo[1]))
            else:
                print("El veterinario ya no tiene ningun paciente")
        else:
            print("\n--Error: Opcion no valida, intente nuevamente\n")
    return 0


def imp_list_Vet():
    print("--Veterinarios activos--")
    re.Lista_Veterinario()


re = Recepcion()


re.nuevo_paciente('Richard Assmann','Mara','Aaron')
re.nuevo_paciente('Erich Hintzsche','Neko','Allen')   #precarga para que haya algo en espera
re.nuevo_paciente('Carl Sachs','Piolin','Alicia')
re.nuevo_paciente('Richard Assmann','Sam','Antonella')

op = 0

while op != 4:

    print("--- Bienvenido a No tengo hijos pero si mascotas ---")
    print("1)Ingresar Mascota")
    print("2)Liberar Mascota")
    print("3)Imprimir Veterianario + Cola de espera")
    print("4)Salir")
    try:
        op = int(input("op:"))
    except ValueError:
        print("--Error, intente nuevamente")
    else:
        if op == 1:
            ingresarmascota()
        elif op == 2:
            liberarmascota()
        elif op == 3:
            imp_list_Vet()
        elif op == 4:
            print("Saliendo...")
        else:
            print("opcion no valida")
