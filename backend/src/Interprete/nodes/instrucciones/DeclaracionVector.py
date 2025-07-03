from backend.src.Interprete.nodes.Nodo import Nodo

class DeclaracionVector(Nodo):
    def __init__(self, tipo, identificador, dimensiones, valores, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.tipo = tipo
        self.identificador = identificador
        self.dimensiones = dimensiones
        self.valores = valores