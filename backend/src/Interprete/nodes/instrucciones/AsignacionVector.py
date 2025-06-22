from backend.src.Interprete.nodes.Nodo import Nodo

class AsignacionVector(Nodo):
    def __init__(self, id, indices, valor, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id
        self.indices = indices
        self.valor = valor