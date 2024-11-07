from arbol import Arbol

def obtener_altura(arbol):
    def altura_recursiva(nodo):
        if nodo is None:
            return 0
        return 1 + max(altura_recursiva(nodo.izquierda), altura_recursiva(nodo.derecha))
    return altura_recursiva(arbol.raiz)
