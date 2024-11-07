from arbol import Arbol

def contar_hojas(arbol):
    def contar_recursivo(nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return contar_recursivo(nodo.izquierda) + contar_recursivo(nodo.derecha)
    return contar_recursivo(arbol.raiz)
