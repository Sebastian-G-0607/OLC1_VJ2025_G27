from backend.src.Interprete.nodes.Nodo import Nodo

class Execute(Nodo):
    def __init__(self, id, args, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id
        self.args = args