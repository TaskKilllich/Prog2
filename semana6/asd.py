import ascii_tree

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.madre = None
        self.padre = None

def construir_arbol_genealogico(persona_raiz):
    arbol = ArbolBinario()
    arbol.raiz = Nodo(persona_raiz)

    cola = []
    cola.append(arbol.raiz)

    while len(cola) > 0:
        nodo_actual = cola.pop(0)

        persona_actual = nodo_actual.valor

        respuesta_madre = input("¿Quién es la madre de " + persona_actual.nombre + "? ")
        if respuesta_madre != "no sé":
            madre = Persona(respuesta_madre)
            persona_actual.madre = madre
            nodo_madre = Nodo(madre)
            nodo_actual.izquierda = nodo_madre
            cola.append(nodo_madre)

        respuesta_padre = input("¿Quién es el padre de " + persona_actual.nombre + "? ")
        if respuesta_padre != "no sé":
            padre = Persona(respuesta_padre)
            persona_actual.padre = padre
            nodo_padre = Nodo(padre)
            nodo_actual.derecha = nodo_padre
            cola.append(nodo_padre)

    return arbol

def imprimir_arbol_genealogico(arbol):
    ascii_tree.generate_tree(arbol.raiz, lambda nodo: nodo.valor.nombre)

# Programa principal
persona_raiz_nombre = input("Ingrese el nombre de la persona raíz: ")
persona_raiz = Persona(persona_raiz_nombre)
arbol_genealogico = construir_arbol_genealogico(persona_raiz)

print("\nÁrbol genealógico:")
imprimir_arbol_genealogico(arbol_genealogico)