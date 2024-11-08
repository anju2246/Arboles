from collections import deque
from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None
        
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    # 1. Obtener altura del árbol (recursivo)
    def obtener_altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if not nodo:
            return 0
        altura_izq = self._altura_recursiva(nodo.izquierdo)
        altura_der = self._altura_recursiva(nodo.derecho)
        return max(altura_izq, altura_der) + 1

    # 2. Retornar nivel de un elemento
    def obtener_nivel(self, valor):
        return self._obtener_nivel_recursivo(self.raiz, valor, 0)
    
    def _obtener_nivel_recursivo(self, nodo, valor, nivel):
        if not nodo:
            return -1
        if nodo.valor == valor:
            return nivel
        nivel_izq = self._obtener_nivel_recursivo(nodo.izquierdo, valor, nivel + 1)
        if nivel_izq != -1:
            return nivel_izq
        return self._obtener_nivel_recursivo(nodo.derecho, valor, nivel + 1)

    # 3. Contar hojas
    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)
    
    def _contar_hojas_recursivo(self, nodo):
        if not nodo:
            return 0
        if not nodo.izquierdo and not nodo.derecho:
            return 1
        return self._contar_hojas_recursivo(nodo.izquierdo) + self._contar_hojas_recursivo(nodo.derecho)

    # 4. Valor más pequeño (no recursivo)
    def valor_minimo_no_recursivo(self):
        if not self.raiz:
            return None
        actual = self.raiz
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual.valor

    # 4. Valor más pequeño (recursivo)
    def valor_minimo_recursivo(self):
        return self._valor_minimo_recursivo(self.raiz)
    
    def _valor_minimo_recursivo(self, nodo):
        if not nodo:
            return None
        if not nodo.izquierdo:
            return nodo.valor
        return self._valor_minimo_recursivo(nodo.izquierdo)

    # 5. Imprimir árbol horizontal
    def imprimir_horizontal(self):
        return self._imprimir_horizontal_recursivo(self.raiz, 0)
    
    def _imprimir_horizontal_recursivo(self, nodo, nivel):
        if not nodo:
            return []
        resultado = []
        resultado.extend(self._imprimir_horizontal_recursivo(nodo.derecho, nivel + 1))
        resultado.append(("  " * nivel) + str(nodo.valor))
        resultado.extend(self._imprimir_horizontal_recursivo(nodo.izquierdo, nivel + 1))
        return resultado

    # 6. Eliminar elemento
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
    
    def _eliminar_recursivo(self, nodo, valor):
        if not nodo:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            if not nodo.izquierdo:
                return nodo.derecho
            elif not nodo.derecho:
                return nodo.izquierdo
            temp = self._encontrar_min(nodo.derecho)
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.valor)
        return nodo
    
    def _encontrar_min(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    # 7. Verificar si dos árboles son idénticos
    def es_identico(self, otro_arbol):
        return self._es_identico_recursivo(self.raiz, otro_arbol.raiz)
    
    def _es_identico_recursivo(self, nodo1, nodo2):
        if not nodo1 and not nodo2:
            return True
        if not nodo1 or not nodo2:
            return False
        return (nodo1.valor == nodo2.valor and 
                self._es_identico_recursivo(nodo1.izquierdo, nodo2.izquierdo) and
                self._es_identico_recursivo(nodo1.derecho, nodo2.derecho))

    # 8. Recorrido en amplitud
    def recorrido_amplitud(self):
        if not self.raiz:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    # 9. Altura sin recursividad
    def altura_no_recursiva(self):
        if not self.raiz:
            return 0
        cola = deque([(self.raiz, 1)])
        max_altura = 0
        while cola:
            nodo, nivel = cola.popleft()
            max_altura = max(max_altura, nivel)
            if nodo.izquierdo:
                cola.append((nodo.izquierdo, nivel + 1))
            if nodo.derecho:
                cola.append((nodo.derecho, nivel + 1))
        return max_altura

 
    # 10. Crear árbol de expresión
    def crear_arbol_expresion(self, expresion):
        def es_operador(c):
            return c in '+-*/^'
        
        def precedencia(c):
            if c in '+-': return 1
            if c in '*/': return 2
            if c == '^': return 3
            return 0
        
        def construir_arbol(expr):
            # Eliminar paréntesis externos si existen
            while expr[0] == '(' and expr[-1] == ')':
                # Verificar si los paréntesis son parte de la estructura
                contador = 0
                balanceado = True
                for i in range(1, len(expr)-1):
                    if expr[i] == '(':
                        contador += 1
                    elif expr[i] == ')':
                        contador -= 1
                    if contador < 0:
                        balanceado = False
                        break
                if contador == 0 and balanceado:
                    expr = expr[1:-1]
                else:
                    break
            
            # Encontrar el operador principal
            operador_pos = -1
            min_precedencia = float('inf')
            parentesis = 0
            
            for i in range(len(expr)):
                if expr[i] == '(':
                    parentesis += 1
                elif expr[i] == ')':
                    parentesis -= 1
                elif parentesis == 0 and es_operador(expr[i]):
                    curr_precedencia = precedencia(expr[i])
                    if curr_precedencia <= min_precedencia:
                        min_precedencia = curr_precedencia
                        operador_pos = i
            
            # Si no hay operador, es un operando
            if operador_pos == -1:
                return Nodo(expr)
            
            # Crear nodo con el operador
            nodo = Nodo(expr[operador_pos])
            
            # Construir subárboles
            nodo.izquierda = construir_arbol(expr[:operador_pos])
            nodo.derecha = construir_arbol(expr[operador_pos + 1:])
            
            return nodo
        
        # Validar que la expresión no esté vacía
        if not expresion:
            raise ValueError("La expresión está vacía")
        
        # Construir el árbol
        self.raiz = construir_arbol(expresion)
        return self.raiz