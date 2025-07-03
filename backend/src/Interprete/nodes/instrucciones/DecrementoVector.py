from backend.src.Interprete.nodes.Nodo import Nodo

class DecrementoVector(Nodo):
    def __init__(self, id, indices, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id
        self.indices = indices