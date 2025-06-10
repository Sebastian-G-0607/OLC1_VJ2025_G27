from backend.src.Interprete.nodes.Nodo import Nodo

class Modulo(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    def __str__(self):
        return f"Modulo(izquierda={self.izquierda}, derecha={self.derecha})"