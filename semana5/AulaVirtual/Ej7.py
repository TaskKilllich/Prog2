"""Ejercicio 7
En el Aula Virtual está definido un Tipo Abstracto de Datos llamado ListaDeAlumnos, que implementa una Lista
Doblemente Enlazada de Alumnos, con los siguientes datos:
Nº de Alumno, DNI, Apellido, Nombre, Código de carrera que cursa, y los finales que tiene rendidos (código de
materia, fecha, nota).
Se definen e implementan las siguientes operaciones para las listas de alumnos:
• Crear una lista de alumnos, inicialmente vacía. La lista mantiene la cantidad de alumnos en un invariante.
• Insertar un alumno en la lista, manteniendo el orden por número de alumno (legajo).
• Borrar de la lista y devolver un alumno (el objeto), utilizando para ello el número de alumno.
• Imprimir la lista, con los datos básicos de cada alumno
Por otro lado, para los alumnos se definen las operaciones de creación y manejo de punteros (próximo, siguiente)
y la impresión del alumno, incluyendo los finales que ha rendido.
También se incluye el programa ListaDeAlumnos_carga que muestra algunas formas posibles de utilizar los
nuevos tipos definidos.
a) Amplía la implementación de tal manera que se pueda agregar una nueva nota de examen final (código de
materia, fecha, nota), utilizando un método y no accediendo a la estructura, como se hace en el programa
carga de ejemplo. Se debe validar la nota (0 -10) y que la materia exista en el diccionario de materias.
b) Escribí un programa que, dado el TAD definido previamente, solicite un numero de alumno e imprima sus datos,
incluyendo los exámenes rendidos y las notas obtenidas. Se debe informar si el alumno no existe en la lista.
Para resolver los ejercicios, se puede extender el TAD con los métodos que consideres necesarios"""

from ListaAlumnos import *
from datetime import datetime
#alu_id,alu_dni,alu_apell,alu_nom,alu_c_cur

def carga_alu():
    print("-- Agregar un alumno al aula --")
    print("Ingrese los sigientes datos del alumno...")
    alu_id = pedir_id()
    alu_id, ya_cargado = checkid(alu_id)
    if alu_id == True:
        print("----------------------------")
        print("Ya existe un alumno con ese id")
        print(ya_cargado)
        print("----------------------------")
        return
    alu_dni = pedir_dni()
    alu_apell , alu_nom = pedir_nom_appe()
    alu_c_cur = pedir_car_cur()
    op = input("El alumno tiene rendido algun final?(s/n)")

    if op.lower() == 's':
        alu_final = pedir_finales()
        Aula_virtual.agregar_alu(alu_id, alu_dni, alu_apell, alu_nom, alu_c_cur, alu_final)
    else:
        Aula_virtual.agregar_alu(alu_id, alu_dni, alu_apell, alu_nom, alu_c_cur)

def pedir_nom_appe():
    alu_apell = input("Ingrese el apellido del alumno:")
    alu_nom = input("Ingerse el Nombre del alumno:")
    alu_apell = alu_apell.capitalize()
    alu_nom = alu_nom.capitalize()
    return alu_apell, alu_nom

def pedir_id():
    alu_id = input("Ingrese el Id del alumno:")
    if len(alu_id) == 0:
        print("intente nuevamente")
        pedir_id()
    return alu_id

def checkid(alu_id):
    check, ya_cargado = Aula_virtual.validar_id(alu_id)
    return check, ya_cargado

def pedir_dni():
    cargacorrecta = False
    while cargacorrecta != True:
        try:
            alu_dni = int(input("DNI (sin puntos):"))
        except ValueError:
            print("Formato o dato no valido, intente nuevamente")
        else:
            if len(str(alu_dni)) < 8:
                print("No es un DNI valido")
            else:
                cargacorrecta = True
    return alu_dni

def pedir_car_cur():
    alu_c_cur = input("Codigo de la carrera:")
    return alu_c_cur

def pedir_finales():
    alu_finales = []
    cargacorrecta = False
    imp_code = input("Escriba 'code' para imprimir los codigos y las materias, apriete enter para no mostrar nada:")
    if imp_code.lower() == 'code':
        Aula_virtual.imprimir_materias()
    while cargacorrecta != True:
        codigo_mat = input("Codigo de materia:")
        codigo_mat = codigo_mat.upper()
        check = Aula_virtual.verifica_code_materia(codigo_mat)
        if check == False:
            print("Error en el codigo de materi, intente nuevamente...")
        else:
            alu_finales.append(codigo_mat)
            while cargacorrecta != True:
                try:
                    print("-* no usar (), si usar /")
                    fecha = input("Ingrese una fecha (dd/mm/yyyy) :")
                    # Convertir la fecha ingresada en un objeto datetime
                    fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
                    # Formatear la fecha en el formato deseado (por ejemplo, dd de mes de yyyy)
                    fecha_formateada = fecha_objeto.strftime("%d - %B - %Y")
                except ValueError:
                    print("Formato de fecha no valido, intente nuevamente")
                else:
                    alu_finales.append(fecha_formateada)
                    while cargacorrecta != True:
                        try:
                            nota = int(input("Nota:"))
                        except ValueError:
                            print("--Error: dato no valido")
                        else:
                            if nota < 0 or nota > 10:
                                print("Ingrese una nota valida")
                            else:
                                alu_finales.append(nota)
                                cargacorrecta = True
    return alu_finales

def eliminar_alu():
    print("-- Eliminar alumno de la lista por id --")
    op = input("Desea imprimir la lista de los alumnos? (s/n):")
    if op.lower() == 's':
        print("-----------------------------")
        Aula_virtual.imprimir_alumnos()
        print("-----------------------------")
    alu_id = input("Ingrese el id del alumno a eliminar:")
    alu_eliminado = Aula_virtual.remove(alu_id)
    if alu_eliminado != None:
        print("-------------------------------------------------")
        print(f"El Alumno:{alu_eliminado} ya no esta en la lista")
        print("-------------------------------------------------")
    return

def imprimir_alu():
    op = 1
    while op != 0:
        print(" --------------------------------------------")
        print("| 1)Imprimir lista de alumnos")
        print("| 2)Imprimir lista de alumnos + que finales rindio")
        print("| 3)Imprimir segun id")
        print("| 0)Volver")
        try:
            op = int(input("| op:"))
        except ValueError:
            print("opcion no valida")
        else:
            print(" -------------------------------------------")
            if op == 1:
                Aula_virtual.imprimir_alumnos()
            elif op == 2:
                Aula_virtual.imprimir_datos()
            elif op == 3:
                alu_id = pedir_id()
                Alu = Aula_virtual.imprimir_segun_id(alu_id)
                if Alu == False:
                    print(f"No existe alumno con el id {alu_id}")
                    return
                Alu.imprimir()
            elif op == 4:
                print("\n")
            else:
                print("opcion no valida")
    return

def aniadir_final():
    op = input("Imprimir lista de alumnos cargados? (s/n):")
    if op.lower() == 's':
        Aula_virtual.imprimir_alumnos()
    id = input("id:")
    check, otro = Aula_virtual.validar_id(id)
    if check == True:
        alu_finales = pedir_finales()
        Aula_virtual.agregar_finales(id,alu_finales)
    else:
        print("No existe alumno que coincida con el id puesto")
    return


fecha_objeto = datetime.strptime("3/2/2022", "%d/%m/%Y")
fecha_formateada = fecha_objeto.strftime("%d - %B - %Y")
Aula_virtual = ListaAlumnos()
Aula_virtual.agregar_alu("24-18-910", 36860458, "Hernández", "Jesica Daiana", 123)
Aula_virtual.agregar_alu("24-18-943", 41040980, "Loncon", "Nahuel Hernan", 123,['IF004',fecha_formateada,7])
Aula_virtual.agregar_alu("24-18-988", 38096837, "Lopez", "Guillermo David", 123)


op = 1
while op != 0:
    print("--- Aula Virtual ---")
    print("1)Cargar un alumno")
    print("2)Sacar a un alumno de la lista")
    print("3)Agregar un final a sierto alumno")
    print("4)Imprimir lista de alumnos")
    print("0)Salir")
    try:
        op = int(input("op:"))
    except ValueError:
        print("-- Error opcion no valida")
    if op == 1:
        carga_alu()
    elif op == 2:
        eliminar_alu()
    elif op == 3:
        aniadir_final()
    elif op == 4:
        imprimir_alu()
    elif op == 0:
        print("Saliendo")
    else:
        print("Ingrese un valor valido")




















