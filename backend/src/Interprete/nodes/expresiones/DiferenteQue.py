from backend.src.Interprete.nodes.Nodo import Nodo

class DiferenteQue(Nodo):
    def __init__(self, izquierda, derecha, linea=None, columna=None):
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f"DiferenteQue({self.izquierda}, {self.derecha})"