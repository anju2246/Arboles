from arbol import Arbol

def valor_menor(arbol):
    nodo = arbol.raiz
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo.valor
