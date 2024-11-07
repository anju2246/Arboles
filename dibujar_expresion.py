from arbol import Arbol, Nodo

def construir_arbol_expresion(expresion):
    operadores = set(['+', '-', '*', '/'])
    pila = []
    for char in expresion:
        if char in operadores:
            nodo = Nodo(char)
            nodo.derecha = pila.pop()
            nodo.izquierda = pila.pop()
            pila.append(nodo)
        else:
            pila.append(Nodo(char))
    return pila.pop()

def dibujar_arbol(canvas, nodo, x, y, dx, dy):
    if nodo:
        canvas.create_text(x, y, text=nodo.valor)
        if nodo.izquierda:
            canvas.create_line(x, y, x - dx, y + dy)
            dibujar_arbol(canvas, nodo.izquierda, x - dx, y + dy, dx // 2, dy)
        if nodo.derecha:
            canvas.create_line(x, y, x + dx, y + dy)
            dibujar_arbol(canvas, nodo.derecha, x + dx, y + dy, dx // 2, dy)
