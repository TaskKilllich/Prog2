"""Ejercicio 9
Implementar el método TopSort visto en clase en alguno de los TAD implementados para grafos (con lista de
adyacencia o con matriz de adyacencia).
Luego, escribir un programa que cargue los datos correspondientes al plan de estudios de la carrera APU y
ejecute el método TopSort. El orden resultante del algoritmo, ¿es similar al estado de sus cursadas? ¿Hay
alguna forma de variar el orden del resultado, según la carga de los datos?"""

from GrafosTopsort import *

materias = {'MA008': 'ELEMENTOS DE LOGICA Y MATEMATICA DISCRETA',
            'MA006': 'ESTADISTICA ',
            'FA007': 'ACREDITACION DE IDIOMA',
            'IF001': 'ELEMENTOS DE INFORMÁTICA',
            'MA045': 'ÁLGEBRA ',
            'IF002': 'EXPRESIÓN DE PROBLEMAS Y ALGORITMOS',
            'IF003': 'ALGORÍTMICA Y PROGRAMACIÓN I',
            'MA046': 'ANÁLISIS MATEMÁTICO',
            'IF004': 'SISTEMAS Y ORGANIZACIONES',
            'IF005': 'ARQUITECTURA DE COMPUTADORAS',
            'IF006': 'ALGORÍTMICA Y PROGRAMACIÓN II',
            'IF007': 'BASES DE DATOS I',
            'IF008': 'PROGRAMACIÓN ORIENTADA A OBJETOS',
            'IF009': 'LABORATORIO DE PROGRAMACIÓN Y LENGUAJES ',
            'IF010': 'ANÁLISIS Y DISEÑO DE SISTEMAS',
            'IF011': 'SISTEMAS OPERATIVOS',
            'IF012': 'DESARROLLO DE SOFTWARE '
            }

graph = Grafo()

graph.insertar("MA006", 'MA045')
graph.insertar("MA006", 'MA046')
graph.insertar("MA006", 'FA007')

graph.insertar('IF003', 'IF002')

graph.insertar('IF004', 'FA007')

graph.insertar('IF005', 'IF001')
graph.insertar('IF005', 'FA007')

graph.insertar('IF006', 'IF003')
graph.insertar('IF006', 'MA008')
graph.insertar('IF006', 'FA007')
graph.insertar('IF006', 'IF002')

graph.insertar('IF007', 'IF006')
graph.insertar('IF007', 'FA007')
graph.insertar('IF007', 'IF003')
graph.insertar('IF007', 'MA008')

graph.insertar('IF008', 'IF006')
graph.insertar('IF008', 'FA007')
graph.insertar('IF008', 'MA008')
graph.insertar('IF008', 'IF003')

graph.insertar('IF009', 'IF008')
graph.insertar('IF009', 'FA007')
graph.insertar('IF009', 'IF006')

graph.insertar('IF010', 'IF004')
graph.insertar('IF010', 'IF007')
graph.insertar('IF010', 'FA007')
graph.insertar('IF010', 'IF006')

graph.insertar('IF011', 'IF005')
graph.insertar('IF011', 'IF006')
graph.insertar('IF011', 'FA007')
graph.insertar('IF011', 'IF001')
graph.insertar('IF011', 'IF003')
graph.insertar('IF011', 'MA008')

graph.insertar('IF012', 'IF010')
graph.insertar('IF012', 'IF008')
graph.insertar('IF012', 'FA007')
graph.insertar('IF012', 'IF004')
graph.insertar('IF012', 'IF006')
graph.insertar('IF012', 'IF007')
print("El orden para cursar las materias podria ser")
TopSort(graph,materias)
print("#materias como algebra analisi y estadistica se podrian hacer en cualquier otro momento ")


