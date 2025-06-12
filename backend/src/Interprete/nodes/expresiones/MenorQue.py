from backend.src.Interprete.nodes.Nodo import Nodo

class MenorQue(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"MenorQue({self.izquierda}, {self.derecha})"