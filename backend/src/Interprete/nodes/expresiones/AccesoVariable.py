from backend.src.Interprete.nodes.Nodo import Nodo

class AccesoVariable(Nodo):
    def __init__(self, id, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id