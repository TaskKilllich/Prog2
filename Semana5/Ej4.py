"""Ejercicio 4
Crear un programa que, usando el TAD definido en el Ejercicio 1, permita a un usuario administrar una lista de
tareas pendientes. Dá la opción de elegir entre las operaciones: agregar tareas, borrar tareas o listar las tareas de
la lista.
Considerá lo siguiente:
• Las tareas se agregan al final de la lista, y llevan un número de ítem de lista y una
descripción. El número se genera automáticamente a partir del número del último elemento
de la lista + 1.
• Se puede borrar una tarea de cualquier lugar de la lista, utilizando el número de ítem.
• La opción de listar muestra todas las tareas pendientes que están en la lista, en el orden en que se
agregaron."""

from ListasEnlazadas import *


def agregartarea():
    dictarea = ["sacar basura","labar ropa","sacar al perro","hacer la cama","cocinar para maniana","ir a la uni"]
    print("--- Agregar tarea a la lista ---")
    print("--Ingrese un * para terminar la carga")
    op = int(input("--Ingrese un 1 para llenar automaticamente\nTarea:"))
    if op == 1:
        print("La lista se lleno con tareas precargadas")
        for i in dictarea:
            taskmanager.agregar_nodo(i)
    else:
        tarea = 0
        while tarea != '*':
            tarea = input("Tarea:")
            if tarea != '*':
                taskmanager.agregar_nodo(tarea)
        print("Volviendo al menu...\n")

    return

def borrartarea():
    print("--- Eliminar tarea ---")
    print("insgrese el numero de la tarea a borrar")
    taskmanager.imprimirlistanumerada()
    op = int(input("num:"))
    nodoborrado = taskmanager.borrar_por_posicion(op)
    if nodoborrado is False:
        print("Lista de Tareas vacia")
        return
    elif nodoborrado == None:
        print("")
        print(f"La tareas:{nodoborrado} a sido borrada")
    return

def administradordetareas():
    taskmanager.imprimirlistanumerada()
    return


taskmanager = ListaEnlazada()
op = 0
while op != 4:
    print("--- Administrador de Tareas ---")
    print("1)agregar tarea")
    print("2)Borrar tarea")
    print("3)Ver tareas")
    print("4)Salir -se perdera la lista creada-")
    try:
        op = int(input("op:"))
    except ValueError:
        print("Error: Opcion no valida, intente nuevamente")
    else:
        if op == 1:
            agregartarea()
        elif op == 2:
            borrartarea()
        elif op == 3:
            administradordetareas()
        elif op == 4:
            print("Saliendo")
        else:
            print("opcion no valida")


