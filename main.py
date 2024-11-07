import tkinter as tk
from arbol import Arbol
from obtener_altura import obtener_altura
from nivel_elemento import nivel_elemento
from contar_hojas import contar_hojas
from valor_menor import valor_menor
from imprimir_horizontal import imprimir_horizontal
from eliminar_elemento import eliminar_elemento
from son_identicos import son_identicos
from recorrido_amplitud import recorrido_amplitud
from altura_no_recursiva import altura_no_recursiva
from dibujar_expresion import construir_arbol_expresion, dibujar_arbol

# Crear instancia del árbol
arbol = Arbol()

def interfaz():
    ventana = tk.Tk()
    ventana.title("Árbol Binario")

    def insertar_nodo():
        valor = int(entry_valor.get())
        arbol.insertar(valor)
        actualizar_arbol()

    def actualizar_arbol():
        imprimir_horizontal(arbol.raiz)

    # Widgets
    entry_valor = tk.Entry(ventana)
    entry_valor.pack()
    
    tk.Button(ventana, text="Agregar Nodo", command=insertar_nodo).pack()
    tk.Button(ventana, text="Altura del Árbol", command=lambda: print(obtener_altura(arbol))).pack()
    tk.Button(ventana, text="Nivel de Elemento", command=lambda: print(nivel_elemento(arbol, int(entry_valor.get())))).pack()
    tk.Button(ventana, text="Contar Hojas", command=lambda: print(contar_hojas(arbol))).pack()
    tk.Button(ventana, text="Valor Menor", command=lambda: print(valor_menor(arbol))).pack()
    tk.Button(ventana, text="Eliminar Elemento", command=lambda: eliminar_elemento(arbol, int(entry_valor.get()))).pack()
    tk.Button(ventana, text="Recorrido en Amplitud", command=lambda: print(recorrido_amplitud(arbol))).pack()
    tk.Button(ventana, text="Altura sin Recursividad", command=lambda: print(altura_no_recursiva(arbol))).pack()

    # Comprobación de árboles idénticos
    arbol2 = Arbol()  # Suponiendo que arbol2 es otro árbol que queremos comparar
    tk.Button(ventana, text="Son Idénticos", command=lambda: print(son_identicos(arbol, arbol2))).pack()

    # Dibujo de expresiones
    canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
    canvas.pack()
    
    def dibujar_expresion_a():
        expresion = "((a * b) + (c / d))"
        raiz_expresion = construir_arbol_expresion(expresion)
        canvas.delete("all")
        dibujar_arbol(canvas, raiz_expresion, 300, 50, 100, 50)

    def dibujar_expresion_b():
        expresion = "(((a + b) + c) + d)"
        raiz_expresion = construir_arbol_expresion(expresion)
        canvas.delete("all")
        dibujar_arbol(canvas, raiz_expresion, 300, 50, 100, 50)

    def dibujar_expresion_c():
        expresion = "(( -a ) + (x + y)) / ((+b) * (c * d))"
        raiz_expresion = construir_arbol_expresion(expresion)
        canvas.delete("all")
        dibujar_arbol(canvas, raiz_expresion, 300, 50, 100, 50)

    tk.Button(ventana, text="Dibujar Expresión A", command=dibujar_expresion_a).pack()
    tk.Button(ventana, text="Dibujar Expresión B", command=dibujar_expresion_b).pack()
    tk.Button(ventana, text="Dibujar Expresión C", command=dibujar_expresion_c).pack()

    ventana.mainloop()

if __name__ == "__main__":
    interfaz()
