from backend.src.Interprete.nodes.Nodo import Nodo

class Procedimiento(Nodo):
    def __init__(self, id, parametros, instrucciones, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones