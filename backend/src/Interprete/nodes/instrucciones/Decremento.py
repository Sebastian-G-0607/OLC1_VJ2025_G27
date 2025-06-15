from backend.src.Interprete.nodes.Nodo import Nodo

class Decremento(Nodo):
    def __init__(self, variable: str, linea = None, columna = None):
        super().__init__(None, linea, columna)
        self.variable = variable