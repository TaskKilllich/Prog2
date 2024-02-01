from ClaseGrafo import *
from GrafosDFS import DFS

migr = Grafo()

migr.insertar("a","e")
migr.insertar("a","b")

migr.insertar("b","c")
migr.insertar("b","d")

migr.insertar("c","f")


migr.imprimir()
print(migr)

padres = DFS(migr,"a")

ordenados = sorted(padres.items()) # La convierte en Tupla!!
print("Hijo", "Padre")
for hijo in ordenados:
    print(" ",hijo[0], "   ", hijo[1])
  
