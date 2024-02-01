"""Ejercicio 8
Usar el algoritmo de Floyd Warshall con el mismo grafo del Ejercicio 7, y verificar que funciona
correctamente. Luego buscar un grafo con un ciclo negativo y verificar que NO funciona. Hacer una traza
que muestre cual es el comportamiento del algoritmo"""

from GrafoWarshall import *


graph = Grafo(5)
print(" -- Floyd Warshall -- ")

graph.insertar_conpeso("A","B", 10)
graph.insertar_conpeso("A","D", 20)

graph.insertar_conpeso("B","D", 5)
graph.insertar_conpeso("C","B", 2)
graph.insertar_conpeso("B","C", 2)
graph.insertar_conpeso("C","E", 15)
graph.insertar_conpeso("D","E", 11)

graph.imprimir()

graph.armar_matriz_desde_lista()
print("La matriz antes de aplicar Floyd es:")
graph.ver_matriz()
print("-------------")

graph.floyd_warshall()
graph.ver_matriz()

print('si se utilizan distancias negativas el algoritmo funciona en el sentido de que no se rompe')
print("pero los resultados no son logicos o los esperados ya que dependiendo las distancias, hay nodos a los que ya no se pueden llegar")
print("se rompe la propiedad del algoritmo que dice que si existe un camino mas corto entre dos vertices a travez de un tercero, este sera el camino mas corto")

