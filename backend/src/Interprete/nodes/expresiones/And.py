from backend.src.Interprete.nodes.Nodo import Nodo

class And(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"({self.izquierda} AND {self.derecha})"

    def __repr__(self):
        return f"And({self.izquierda}, {self.derecha})"