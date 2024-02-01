from ClaseGrafo import *
from GrafosTopSortQ import *

dgd = True

migr = Grafo(dgd)

migr.insertar("J1","J3", dgd)
migr.insertar("J1","J2", dgd)
migr.insertar("J2","J6", dgd)
migr.insertar("J2","J5", dgd)
migr.insertar("J2","J4", dgd)
migr.insertar("J3","J4", dgd)
migr.insertar("J4","J5", dgd)
migr.insertar("J5","J7", dgd)

migr.imprimir()
print(migr)

print()
print("Algoritmo Topsort")
print("=================")

TopSortQ(migr)

  
