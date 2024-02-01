from ClaseGrafo import *
from GrafosBFS import BFS

migr = Grafo()

migr.insertar("a","e")
migr.insertar("a","d")
migr.insertar("a","c")
migr.insertar("a","b")

migr.insertar("b","e")
migr.insertar("b","d")

migr.insertar("c","g")
migr.insertar("c","f")

migr.insertar("d","e")

migr.insertar("f","g")

migr.imprimir()
print(migr)

padres = BFS(migr,"a")

ordenados = sorted(padres.items()) # La convierte en Tupla!!
print("Hijo", "Padre")
for hijo in ordenados:
    print(" ",hijo[0], "   ", hijo[1])
  
