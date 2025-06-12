from backend.src.Interprete.nodes.Nodo import Nodo

class Suma(Nodo):
    # NODO PARA LA OPERACIÓN DE SUMA
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.izquierda = izquierda  # Operando izquierdo
        self.derecha = derecha      # Operando derecho

    def __repr__(self):
        return f"Suma({self.izquierda!r}, {self.derecha!r})"