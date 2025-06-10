from backend.src.Interprete.nodes.Nodo import Nodo

class MenorIgualQue(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"MenorIgualQue({self.izquierda}, {self.derecha})"

    def __repr__(self):
        return self.__str__()