from backend.src.Interprete.nodes.Nodo import Nodo

class AccesoVariable(Nodo):
    def __init__(self, id, linea=None, columna=None):
        super().__init__(linea, columna)
        self.id = id