"""Ejercicio 7
Transcribir el algoritmo de Dijkstra cuyo código se encuentra en la teoría, y verificar que NO funciona para
grafos con peso negativo. Hacer una traza que muestre cual es el comportamiento del algoritmo."""

from GrafoDijkstra import *

def armar_grafo():

    terminar = False
    print("Ingrese un * para terminar")
    while not terminar:
        ordespeso = input("Origen,Destino,Distancia:")
        if ordespeso == '*':
            terminar = True
        else:
            ordespeso = ordespeso.split(',')

            if len(ordespeso) != 3:
                print("Error: origen o destino mal cargado")
            else:
                graph.insertar_conpeso(ordespeso[0], ordespeso[1], int(ordespeso[2]), True)
    return


graph = Grafo()
print(" -- Algoritmo Dijkstra --")
print("Debera carfar los datos como: origen,destino,distancia entre (origen y destono)  ej:a,b,10")
#armar_grafo()
graph.insertar_conpeso("A","B", 10)
graph.insertar_conpeso("A","D", 20)
graph.insertar_conpeso("B","D", 5)
graph.insertar_conpeso("C","B", 2)
graph.insertar_conpeso("B","C", 2)
graph.insertar_conpeso("C","E", 15)
graph.insertar_conpeso("D","E", 11)
graph.imprimir()

distancias = Dijkstra(graph, "A")

print(distancias)
graph = Grafo()  #recetear el grafo?
print("--------------------------------")
armar_grafo()
vert = None
while vert != '*':
    vert = input("calcular distancia minima usando Dijkstra para el vertice:")
    if vert != '*':
        distancias = Dijkstra(graph, vert)
        print(distancias)


print("#El algoritmo al ingresarle distancias negativas como programa no se rompe pero los resultados al "
      "calcular las distancias mas optimas no son lo esperado, las distancias no pueden ser negativas "
      "y los costes por llegar a un lugar deben ser tomados como valores positivos, tambien si se da el caso de que "
      "por ejemplo para llegar de A->C perderia -2000 pero si voy por A->B->C solo pierdo solo -500,"
      " va a elegir como mejor camino el de A->C ya que -2000 es menor a -500, "
      "el algoritmo no esta diseñado  para manejar valores negativos")