from arbol import Arbol

def nivel_elemento(arbol, valor):
    def buscar_nivel(nodo, valor, nivel):
        if nodo is None:
            return -1
        if nodo.valor == valor:
            return nivel
        izq = buscar_nivel(nodo.izquierda, valor, nivel + 1)
        if izq != -1:
            return izq
        return buscar_nivel(nodo.derecha, valor, nivel + 1)
    return buscar_nivel(arbol.raiz, valor, 0)
