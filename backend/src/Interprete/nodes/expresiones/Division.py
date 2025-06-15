from backend.src.Interprete.nodes.Nodo import Nodo

class Division(Nodo):
    # NODO PARA LA OPERACIÓN DE DIVISIÓN
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.izquierda = izquierda  # Operando izquierdo
        self.derecha = derecha      # Operando derecho

    def __repr__(self):
        return f"Division({self.izquierda!r}, {self.derecha!r})"