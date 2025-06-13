from backend.src.Interprete.nodes.Nodo import Nodo

class Break(Nodo):
    def __init__(self, valor ,linea=None, columna=None):
        super().__init__(linea, columna)
        self.valor = valor