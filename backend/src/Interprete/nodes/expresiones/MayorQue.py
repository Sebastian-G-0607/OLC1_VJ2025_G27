from backend.src.Interprete.nodes.Nodo import Nodo

class MayorQue(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    
    def __str__(self):
        return f"MayorQue(izquierda={self.izquierda}, derecha={self.derecha})"