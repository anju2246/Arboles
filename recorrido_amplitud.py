from arbol import Arbol
from collections import deque

def recorrido_amplitud(arbol):
    if arbol.raiz is None:
        return []
    cola = deque([arbol.raiz])
    resultado = []
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izquierda:
            cola.append(nodo.izquierda)
        if nodo.derecha:
            cola.append(nodo.derecha)
    return resultado
