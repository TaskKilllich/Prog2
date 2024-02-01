""""""
preguntas = {
1: "¿Qué nodos son hojas?",
2: "¿Cuál nodo es la raíz?",
3: "¿Quién es el padre del nodo C?",
4: "¿Que nodos son hijos de C?",
5: "¿Qué nodos son ancestros de E?",
6: "¿Qué nodos son descendientes de E?",
7: "¿Cual es la profundidad del nodo C?",
8: "¿Cual es la altura del nodo C?"}
print("--- Preguntas ---")
for num, preg in preguntas.items():
    print(num, preg)
print("\n--- Respuestas ---")
print("1) Los nodos hojas son: 'D','M','N','J','K','L'")
print("2) El nodo raiz es el primer elemento: 'A'")
print("3) El padre de C es la Raiz: 'A'")
print("4) Los nodos hijos de C son: 'F', 'G', 'H'")
print("5) Los ancestros de E son: 'B','A'")
print("6) Los decendientes de E son: 'I', 'M', 'N'")
print("7) La profundidad de C es de 1")
print("8) La altura hasta el nodo C es de 2")


