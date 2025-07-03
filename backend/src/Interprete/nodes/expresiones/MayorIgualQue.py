from backend.src.Interprete.nodes.Nodo import Nodo

class MayorIgualQue(Nodo):
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"MayorIgualQue({self.izquierda}, {self.derecha})"

    def __repr__(self):
        return self.__str__()