from arbol import Arbol, Nodo

def son_identicos(arbol1, arbol2):
    def comparar_nodos(nodo1, nodo2):
        if nodo1 is None and nodo2 is None:
            return True
        if nodo1 is not None and nodo2 is not None:
            return (nodo1.valor == nodo2.valor and
                    comparar_nodos(nodo1.izquierda, nodo2.izquierda) and
                    comparar_nodos(nodo1.derecha, nodo2.derecha))
        return False
    return comparar_nodos(arbol1.raiz, arbol2.raiz)
