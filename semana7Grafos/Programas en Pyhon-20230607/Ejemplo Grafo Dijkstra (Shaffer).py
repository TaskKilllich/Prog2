from Gra import *
from GrafosDijkstra import *

dgd = True

migr = Grafo(dgd)

migr.insertar("A","B", 10)
migr.insertar("A","D", 20)
migr.insertar("A","C", 3)
migr.insertar("B","D", 5)
migr.insertar("C","B", 2)
migr.insertar("C","E", 15)
migr.insertar("D","E", 11)

migr.imprimir_con_peso()
print(migr)

print()
print("Algoritmo Dijkstra")
print("==================")

distancias = Dijkstra(migr, "A")

print(distancias)

  
