import tkinter as tk
from arbol import Arbol, Nodo

 def dibujar_arbol(canvas, nodo, x, y, espacio_x=100, espacio_y=50):
    if nodo is not None:
        # Dibuja el nodo actual
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
        canvas.create_text(x, y, text=str(nodo.valor))

        # Dibuja la línea y el nodo izquierdo si existe
        if nodo.izquierdo:
            canvas.create_line(x, y, x - espacio_x, y + espacio_y)
            dibujar_arbol(canvas, nodo.izquierdo, x - espacio_x, y + espacio_y, espacio_x // 2, espacio_y)

        # Dibuja la línea y el nodo derecho si existe
        if nodo.derecho:
            canvas.create_line(x, y, x + espacio_x, y + espacio_y)
            dibujar_arbol(canvas, nodo.derecho, x + espacio_x, y + espacio_y, espacio_x // 2, espacio_y)
 

def actualizar_dibujo_arbol(canvas, arbol):
    canvas.delete("all")
    if arbol.raiz is not None:
        dibujar_arbol(canvas, arbol.raiz, x=400, y=50, espacio_x=100, espacio_y=50)

ventana = tk.Tk()
ventana.title("Árbol Binario")

canvas = tk.Canvas(ventana, width=800, height=600, bg="white")
canvas.pack()

arbol = Arbol()

entry_valor = tk.Entry(ventana)
entry_valor.pack()

def agregar_elemento():
    valor = int(entry_valor.get())
    arbol.insertar(valor)
    actualizar_dibujo_arbol(canvas, arbol)

btn_agregar = tk.Button(ventana, text="Agregar Elemento", command=agregar_elemento)
btn_agregar.pack()

def eliminar_elemento():
    valor = int(entry_valor.get())
    eliminar_nodo(arbol, valor)
    actualizar_dibujo_arbol(canvas, arbol)

btn_eliminar = tk.Button(ventana, text="Eliminar Elemento", command=eliminar_elemento)
btn_eliminar.pack()

ventana.mainloop()
