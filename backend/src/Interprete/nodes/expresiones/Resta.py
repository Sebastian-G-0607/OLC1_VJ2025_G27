from backend.src.Interprete.nodes.Nodo import Nodo

class Resta(Nodo):
    # NODO PARA LA OPERACIÓN DE RESTA
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda  # Operando izquierdo
        self.derecha = derecha      # Operando derecho

    def __repr__(self):
        return f"Resta({self.izquierda!r}, {self.derecha!r})"