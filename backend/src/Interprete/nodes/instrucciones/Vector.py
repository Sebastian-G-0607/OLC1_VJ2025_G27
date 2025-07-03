from backend.src.Interprete.nodes.Nodo import Nodo

class Vector(Nodo):
    def __init__(self, elementos, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.elementos = elementos