"""Ejercicio 10
Podemos representar naturalmente las ciudades de un mapa caminero con un grafo, y hacer cálculos de
distancia y selección de caminos, a partir de este grafo.
Dado el plano de ciudades del noroeste del Chubut de la figura, y las dos tablas de distancias,
(a) Usando el TAD grafo, cargar los datos correspondientes.
(b) Ejecutar el algoritmo de Dijkstra del Ejercicio 7 e imprimir una tabla que muestre las
distancias de Esquel a todas las otras ciudades o puntos del camino.
(c) Ejecutar el algoritmo de Floyd Warshall del Ejercicio 8 e imprimir una tabla que muestre las
distancias de Esquel a todas las otras ciudades o puntos del camino.
(d) Escribir un programa que solicite una ciudad cualquiera e imprima las distancias hasta las
otras ciudades o puntos del mapa"""


from GrafosMatrices import *


'def cargar_chuwut(lista):
    for i in lista:
        ordesdis = i.split(',')
        chuwut.insertar_conpeso(ordesdis[0], ordesdis[1], int(ordesdis[2]))
    print("La Matriz de las distancias:")
    chuwut.armar_matriz_desde_lista()


def mosrtar_Dijkstra_Esquel():
    msj = Dijkstra(chuwut, 'A', ciudades)
    for i in msj:
        print(i)
    return


def mostrar_Warshall_Esquel():
    chuwut.floyd_warshall()
    chuwut.ver_matriz()
    chuwut.washall_de_un_punto('A')
    return


def mostrar_Warshall(city):
    chuwut.washall_de_un_punto(city)
    return


def mosrtar_Dijkstra(city):
    msj = Dijkstra(chuwut, city, ciudades)
    for i in msj:
        print(i)
    return


chuwut = Grafo()
lista = ['A,B,24', 'A,C,24', 'A,E,97', 'A,F,94', 'B,C,15', 'B,D,64', 'C,G,95', 'D,E,75', 'F,G,35', 'F,H,27', 'F,J,39',
         'G,H,30', 'H,I,7', 'I,J,39']

ciudades = {'A': 'Esquel', 'B': 'Trevelin',
            'C': 'Cruce al Lago', 'D': 'Corcovado',
            'E': 'Tecka', 'F': 'Puesto Leleque',
            'G': 'Cholila', 'H': 'Cruce Los Retamos',
            'I': 'Epuyén', 'J': 'El Maitén'}
cargar_chuwut(lista)
print('-----------------------------------------------------------------------------------')
print(" -- PARA ESQUEL --")
mosrtar_Dijkstra_Esquel()
print('-----------------------------------------------------------------------------------')
mostrar_Warshall_Esquel()


#mostrar para cualquier ciudad...
terminar = False
while not terminar:
    print('--------------------------------------------------------------------------------------------------------')
    city = input("ver recorrido para otra ciudad segun su vertice\n 1) para imprimir la lista de las ciudades\nciudad:")
    if city == '1':
        for key,ciudad in ciudades.items():
            print(f'{key} - {ciudad}')

    elif city.upper() in ciudades.keys():
        print(f"Las distancias minimas para {ciudades.get(city)} a cada una de las ciudades son:")
        mosrtar_Dijkstra(city)
        mostrar_Warshall(city)

    elif city.capitalize() in ciudades.values():
        for key, value in ciudades.items():
            if value == city.capitalize():  #feo pero no se me ocurrio como obtener la key a partir del valor
                clave = key

        print(f"Las distancias minimas para {ciudades.get(clave)} a cada una de las ciudades son:")
        mosrtar_Dijkstra(clave)
        mostrar_Warshall(clave)
    elif city == '*':
        terminar = True
    else:
        print("Error ciudad no encontrada")'
