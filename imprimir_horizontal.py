from arbol import Arbol

def imprimir_horizontal(nodo, nivel=0):
    if nodo is not None:
        imprimir_horizontal(nodo.derecha, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.valor)
        imprimir_horizontal(nodo.izquierda, nivel + 1)
