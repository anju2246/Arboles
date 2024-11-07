from arbol import Arbol, Nodo

def eliminar_elemento(arbol, valor):
    def eliminar_nodo(nodo, valor):
        # Caso base: si el árbol está vacío
        if nodo is None:
            return nodo

        # Si el valor a eliminar es menor que el valor del nodo, busca en el subárbol izquierdo
        if valor < nodo.valor:
            nodo.izquierda = eliminar_nodo(nodo.izquierda, valor)

        # Si el valor a eliminar es mayor que el valor del nodo, busca en el subárbol derecho
        elif valor > nodo.valor:
            nodo.derecha = eliminar_nodo(nodo.derecha, valor)

        # Si el valor es igual al valor del nodo, entonces este es el nodo que se debe eliminar
        else:
            # Caso 1: Nodo con un solo hijo o sin hijos
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 2: Nodo con dos hijos
            # Obtener el valor más pequeño en el subárbol derecho (sucesor)
            sucesor = nodo.derecha
            while sucesor.izquierda:
                sucesor = sucesor.izquierda

            # Reemplazar el valor del nodo con el valor del sucesor
            nodo.valor = sucesor.valor

            # Eliminar el sucesor
            nodo.derecha = eliminar_nodo(nodo.derecha, sucesor.valor)

        return nodo

    # Llamar a la función auxiliar para eliminar el nodo
    arbol.raiz = eliminar_nodo(arbol.raiz, valor)
