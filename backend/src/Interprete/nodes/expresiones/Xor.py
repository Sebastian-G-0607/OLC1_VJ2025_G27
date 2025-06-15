from backend.src.Interprete.nodes.Nodo import Nodo

class Xor(Nodo):
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"({self.izquierda} XOR {self.derecha})"

    def __repr__(self):
        return f"Xor({self.izquierda}, {self.derecha})"