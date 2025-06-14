from backend.src.Interprete.nodes.Nodo import Nodo

class IgualQue(Nodo):
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"({self.izquierda} == {self.derecha})"