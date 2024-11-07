from arbol import Arbol
from collections import deque

def altura_no_recursiva(arbol):
    if arbol.raiz is None:
        return 0
    cola = deque([(arbol.raiz, 1)])
    altura = 0
    while cola:
        nodo, nivel = cola.popleft()
        altura = max(altura, nivel)
        if nodo.izquierda:
            cola.append((nodo.izquierda, nivel + 1))
        if nodo.derecha:
            cola.append((nodo.derecha, nivel + 1))
    return altura
