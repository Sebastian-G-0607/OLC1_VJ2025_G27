from backend.src.Interprete.nodes.Nodo import Nodo

class Execute(Nodo):
    _contador = 0

    def __init__(self, id, args, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.identificador = id
        self.args = args
        Execute._contador += 1
        self.id = Execute._contador