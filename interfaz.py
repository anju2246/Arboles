import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from arbol import ArbolBinario

class InterfazArbol:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Árbol Binario")
        
        # Configurar el tamaño inicial de la ventana
        self.root.geometry("800x600")
        
        # Frame principal
        self.frame_principal = ttk.Frame(self.root, padding="5")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Frame para controles
        self.frame_controles = ttk.Frame(self.frame_principal)
        self.frame_controles.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Primera fila de controles
        frame_fila1 = ttk.Frame(self.frame_controles)
        frame_fila1.grid(row=0, column=0, columnspan=4, pady=2)
        
        ttk.Label(frame_fila1, text="Valor:").pack(side=tk.LEFT, padx=2)
        self.valor = tk.StringVar()
        self.entrada_valor = ttk.Entry(frame_fila1, textvariable=self.valor, width=10)
        self.entrada_valor.pack(side=tk.LEFT, padx=2)
        
        ttk.Button(frame_fila1, text="Insertar", command=self.insertar, width=10).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_fila1, text="Eliminar", command=self.eliminar, width=10).pack(side=tk.LEFT, padx=2)
        
        # Segunda fila de controles
        frame_fila2 = ttk.Frame(self.frame_controles)
        frame_fila2.grid(row=1, column=0, columnspan=4, pady=2)
        
        ttk.Button(frame_fila2, text="Altura", command=self.mostrar_altura, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_fila2, text="Hojas", command=self.mostrar_hojas, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_fila2, text="Mínimo", command=self.mostrar_minimo, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_fila2, text="Amplitud", command=self.mostrar_amplitud, width=8).pack(side=tk.LEFT, padx=2)
        
        # Tercera fila para expresiones
        frame_fila3 = ttk.Frame(self.frame_controles)
        frame_fila3.grid(row=2, column=0, columnspan=4, pady=2)
        
        ttk.Label(frame_fila3, text="Expresión:").pack(side=tk.LEFT, padx=2)
        self.expresion = tk.StringVar()
        self.entrada_expresion = ttk.Entry(frame_fila3, textvariable=self.expresion, width=30)
        self.entrada_expresion.pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_fila3, text="Crear Árbol de Expresión", 
                  command=self.crear_arbol_expresion, width=20).pack(side=tk.LEFT, padx=2)
        
        # Frame para visualización
        self.frame_visual = ttk.Frame(self.frame_principal)
        self.frame_visual.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.frame_principal.grid_rowconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(0, weight=1)
        
        # Configurar el área de visualización
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_visual)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.frame_visual.grid_rowconfigure(0, weight=1)
        self.frame_visual.grid_columnconfigure(0, weight=1)
        
        # Inicializar árbol
        self.arbol = ArbolBinario()

    def _calcular_posiciones(self):
        """Calcula las posiciones x,y para cada nodo del árbol respetando la estructura BST"""
        if not self.arbol.raiz:
            return {}
        
        # Inicializar el diccionario de posiciones
        pos = {}
        
        def calcular_pos_recursivo(nodo, x, y, width):
            if nodo:
                # Guardar la posición actual
                pos[str(nodo.valor)] = (x, y)
                
                # Calcular el nuevo ancho para los subárboles
                new_width = width / 2
                
                # Calcular las posiciones para los hijos
                # Hijo izquierdo: se mueve a la izquierda y abajo
                if nodo.izquierdo:
                    calcular_pos_recursivo(nodo.izquierdo, x - new_width, y - 0.2, new_width)
                
                # Hijo derecho: se mueve a la derecha y abajo
                if nodo.derecho:
                    calcular_pos_recursivo(nodo.derecho, x + new_width, y - 0.2, new_width)
        
        # Comenzar desde la raíz
        calcular_pos_recursivo(self.arbol.raiz, 0.5, 0.9, 0.4)
        return pos

    def actualizar_visualizacion(self):
        """Actualiza la visualización del árbol"""
        self.ax.clear()
        if self.arbol.raiz:
            G = nx.Graph()
            self._construir_grafo(self.arbol.raiz, G)
            
            # Obtener posiciones personalizadas
            pos = self._calcular_posiciones()
            
            # Dibujar las aristas primero
            edge_labels = {}
            for edge in G.edges():
                nodo1, nodo2 = edge
                # Determinar si es hijo izquierdo o derecho
                if self._es_hijo_izquierdo(nodo1, nodo2) or self._es_hijo_izquierdo(nodo2, nodo1):
                    edge_labels[edge] = 'izq'
                else:
                    edge_labels[edge] = 'der'
            
            # Dibujar el grafo
            nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.0)
            
            # Dibujar los nodos
            nx.draw_networkx_nodes(G, pos,
                                 node_color='lightblue',
                                 node_size=1000,
                                 edgecolors='black')
            
            # Añadir las etiquetas de los nodos
            nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
            
            # Ajustar los límites del gráfico
            self.ax.set_xlim(-0.1, 1.1)
            self.ax.set_ylim(-0.1, 1.1)
        
        # Eliminar los ejes
        self.ax.axis('off')
        
        # Ajustar los márgenes
        plt.tight_layout()
        
        # Actualizar el canvas
        self.canvas.draw()

    def _es_hijo_izquierdo(self, valor_padre, valor_hijo):
        """Determina si valor_hijo es hijo izquierdo de valor_padre"""
        nodo_padre = self._encontrar_nodo(self.arbol.raiz, int(valor_padre))
        return nodo_padre and nodo_padre.izquierdo and str(nodo_padre.izquierdo.valor) == valor_hijo

    def _encontrar_nodo(self, nodo, valor):
        """Encuentra un nodo con el valor dado"""
        if not nodo or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._encontrar_nodo(nodo.izquierdo, valor)
        return self._encontrar_nodo(nodo.derecho, valor)

    def _construir_grafo(self, nodo, G, padre=None):
        """Construye el grafo NetworkX a partir del árbol"""
        if nodo:
            G.add_node(str(nodo.valor))
            if padre:
                G.add_edge(str(padre.valor), str(nodo.valor))
            self._construir_grafo(nodo.izquierdo, G, nodo)
            self._construir_grafo(nodo.derecho, G, nodo)

    def insertar(self):
        """Inserta un nuevo valor en el árbol"""
        try:
            valor = int(self.valor.get())
            self.arbol.insertar(valor)
            self.actualizar_visualizacion()
            self.valor.set("")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido")

    def eliminar(self):
        """Elimina un valor del árbol"""
        try:
            valor = int(self.valor.get())
            self.arbol.eliminar(valor)
            self.actualizar_visualizacion()
            self.valor.set("")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido")

    def crear_arbol_expresion(self):
        """Crea un árbol a partir de una expresión matemática"""
        expresion = self.expresion.get().replace(" ", "")
        if expresion:
            try:
                self.arbol = ArbolBinario()
                self.arbol.crear_arbol_expresion(expresion)
                self.actualizar_visualizacion()
                self.expresion.set("")
            except Exception as e:
                messagebox.showerror("Error", f"Error al procesar la expresión: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una expresión")

    def mostrar_altura(self):
        """Muestra la altura del árbol"""
        altura = self.arbol.obtener_altura()
        messagebox.showinfo("Altura", f"La altura del árbol es: {altura}")

    def mostrar_hojas(self):
        """Muestra el número de hojas del árbol"""
        hojas = self.arbol.contar_hojas()
        messagebox.showinfo("Hojas", f"El número de hojas es: {hojas}")

    def mostrar_minimo(self):
        """Muestra el valor mínimo del árbol"""
        minimo = self.arbol.valor_minimo_no_recursivo()
        messagebox.showinfo("Valor Mínimo", f"El valor mínimo es: {minimo}")

    def mostrar_amplitud(self):
        """Muestra el recorrido en amplitud del árbol"""
        recorrido = self.arbol.recorrido_amplitud()
        messagebox.showinfo("Recorrido en Amplitud", f"Recorrido: {recorrido}")